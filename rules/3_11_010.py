from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    if float(record.objectInfo["人均纯收入（元）"]) < 4000:
        raise Error(no="3_11_010", objectInfo=[record.objectInfo])
