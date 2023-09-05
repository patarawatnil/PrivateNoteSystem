import datetime
from database.connectdb import connect_db

db = connect_db()
col = db["Notes"]


def create_new_note(user_id, title, content, created_date):
    new_note = {"title": title, "content": content, "createdDate": created_date, "updatedDate": created_date,
                "user_id": user_id}
    col.insert_one(new_note)


def find_one_note(note_id):
    rs = col.find_one({"_id": note_id})
    return rs


def find_from_search(user_id, keyword="", from_date=datetime.datetime.min):
    user = {"user_id": user_id}
    search_word = {
        "$or": [{"title": {"$regex": keyword, "$options": "i"}}, {"content": {"$regex": keyword, "$options": "i"}}]}
    search_from_date = {"createdDate": {"$gte": from_date, "$lte": datetime.datetime.utcnow()}}
    rs = col.find({"$and": [user, search_word, search_from_date]}, {"content": 0}).sort([("createdDate", -1)])
    return rs


def update_note_by_id(note_id, title, content, updated_date):
    key = {"_id": note_id}
    update = {"$set": {
        "title": title,
        "content": content,
        "updatedDate": updated_date
    }}
    col.update_one(key, update)


def delete_note_by_id(note_id):
    col.delete_one({"_id": note_id})
