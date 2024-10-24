#!/usr/bin/env python3
"""
nginx logs module
"""
from pymongo import MongoClient


def nginx_log_stats():
    """ Provides some stats about Nginx logs stored in MongoDB """
    # Connect to MongoDB
    client = MongoClient()
    db = client['logs']
    nginx_collection = db['nginx']

    # Get total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Define HTTP methods to check
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("Methods:")

    # Count logs for each method
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\t{method_count}: {method}")

    # Count status checks
    total_status_checks = nginx_collection.count_documents({"path": "/status"})
    print(f"\t{total_status_checks} status check")


if __name__ == "__main__":
    nginx_log_stats()
