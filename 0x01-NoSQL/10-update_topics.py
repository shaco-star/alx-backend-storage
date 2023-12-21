#!/usr/bin/env python3

"""Task 10 """


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school
    document based on the name"""
    query = {"name": name}
    change = {"$set": {"topics": topics}}
    changed = mongo_collection(query, change)
