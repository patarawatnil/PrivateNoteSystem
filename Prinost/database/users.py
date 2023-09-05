import datetime, hashlib

from database.connectdb import connect_db

db = connect_db()
col = db["Users"]


def create_new_user_account(user, email, password):
    password = hashlib.sha256(password.encode())
    password = password.hexdigest()
    now = datetime.datetime.utcnow()
    new_account = {"username": user, "email": email, "hashpass": password, "createdDate": now, "lastAccess": now}
    col.insert_one(new_account)


def is_user_exists(new_user):
    rs = col.find_one({"username": new_user}, {"username": 1})
    if rs is None:
        return False
    return True


def is_email_exists(new_email):
    rs = col.find_one({"email": new_email}, {"email": 1})
    if rs is None:
        return False
    return True


def is_auth(username, password):
    password = hashlib.sha256(password.encode())
    password = password.hexdigest()
    rs = col.find_one({"$and": [{"$or": [{"username": username}, {"email": username}]}, {"hashpass": password}]})
    if rs is not None:
        key = {"_id": rs["_id"]}
        last_access = {"$set": {"lastAccess": datetime.datetime.utcnow()}}
        col.update_one(key, last_access)
        return True, rs
    return False, None
