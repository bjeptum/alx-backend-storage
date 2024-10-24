#!/usr/bin/env python3
"""
mongo_collection module
"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """Return the list of school having a specific topic"""
    results = mongo_collection.find(
            {"topics": topic}
            )
    return [result for result in results]
