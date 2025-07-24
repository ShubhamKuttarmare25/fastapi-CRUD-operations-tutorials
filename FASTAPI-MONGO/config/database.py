from pymongo import MongoClient


client = MongoClient("mongodb+srv://shubhamk9240:shubham123@cluster0.n5ub3l5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.todo_db


collection_name = db["todo_collection"]




