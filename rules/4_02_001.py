from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["户联系电话"] == "" or len(record.objectInfo["户联系电话"]) != 11:
        raise Error(no='4_01_001', objectInfo=[record.objectInfo])
