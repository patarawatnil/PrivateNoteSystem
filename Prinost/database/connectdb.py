import pymongo


def connect_db():
    username = "general_user"
    password = "ZeSmGHoBxX8uXTXs"
    url = "mongodb+srv://<username>:<password>@cluster0-l7gnh.mongodb.net/test?retryWrites=true&w=majority"
    url = url.replace("<username>", username).replace("<password>", password)
    client = pymongo.MongoClient(url)
    db = client.get_database("Prinost")
    return db
