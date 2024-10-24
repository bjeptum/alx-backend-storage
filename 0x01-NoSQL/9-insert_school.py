#!/usr/bin/env python3
"""
mongo_collection module
"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document based on kwargs """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
