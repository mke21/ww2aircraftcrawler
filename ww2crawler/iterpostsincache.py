"""
A way to iterate over all downloaded posts
"""
import os
import json

def file_iter(path):
    """
    Iterates over files and returns hard paths
    Will go only 1 level deep
    """
    for filename in os.listdir(path):
        if filename.endswith(".json"):
            yield os.path.join(path, filename)


def lcase(obj):
    obj['text'] = obj['text'].lower()
    return obj


def read_files(path):
    """
    reads files and returns datastructure
    path is dir in which jsons are saved
    will lowercase all content
    """
    for f in file_iter(path):
        print (f)
        yield map(
            lcase,
            json.load(
                open(f)
            )
        )

def readposts(path):
    """
    Yields single posts of all files
    """
    for posts in read_files(path):
        for p in posts:
            yield p
            
