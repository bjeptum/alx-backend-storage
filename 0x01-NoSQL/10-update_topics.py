#!/usr/bin/env python3
"""
mongo_collection module
"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """Changes all topics of document based on field"""
    result = mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
            )
    return result.modified_count
