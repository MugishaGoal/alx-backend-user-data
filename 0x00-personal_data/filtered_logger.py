#!/usr/bin/env python3
"""A function that returns the log message obfuscated"""


import re


def filter_datum(fields, redaction, message, separator):
    """Returns the log message obfuscated"""
    for field in fields:
        message = re.sub(fr'(?<={field}=)[^{separator}]+', redaction, message)
    return message