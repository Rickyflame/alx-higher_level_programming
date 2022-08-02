#!/usr/bin/python3
"""Defines a function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Creates a python object from a json file"""
    with open(filename) as f:
        return json.load(f)
