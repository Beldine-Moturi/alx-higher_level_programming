#!/usr/bin/python3
"""Defines a function ``to_json_string()``"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object my_obj (string)"""

    return json.dumps(my_obj)
