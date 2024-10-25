#!/usr/bin/env python3
"""
Top students module.
"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """Return all students sorted by average score"""
    # Find all students and calculate average scores
    students = []
    results = mongo_collection.find()
    for student in results:
        topics = student.get("topics", [])
        scores = [topic["score"] for topic in topics
                  if "score" in topic]

        if scores:
            avg_score = sum(scores) / len(scores)
        else:
            avg_score = 0
        student["averageScore"] = avg_score
        students.append(student)

    # Sort avg_score in descending order
    students.sort(key=lambda x: x["averageScore"], reverse=True)

    return students
