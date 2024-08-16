import os
import random

def load_image_paths(directory):
    image_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            ..........
    return image_paths

def load_comments(file_path):
    with open(file_path, "r") as file:
        ..........
    return comments

def shuffle_arrays(image_paths, comments):
    random.shuffle(image_paths)
    ..........

image_paths = load_image_paths("Data/images")
comments = load_comments("Data/comments.txt")

def get_image_path_and_comment():
    global image_paths, comments
    
    ..........
        comments = load_comments("Data/comments.txt")
        print("Loaded comments again since count was 0")
    
    image_path = image_paths.pop(0) if image_paths else None
    ..........
    return image_path, comment

class EmptyCommentsFile(Exception):
    pass