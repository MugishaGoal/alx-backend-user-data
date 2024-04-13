#!/usr/bin/env python3
"""A function that returns the log message obfuscated"""


import logging
import re


def filter_datum(fields, redaction, message, separator):
    """Returns the log message obfuscated"""
    for field in fields:
        message = re.sub(fr'(?<={field}=)[^{separator}]+', redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"

    def __init__(self, fields):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format the log record, redacting specified fields """
        log_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, log_message, self.SEPARATOR)