from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["与户主关系"] == "":
        raise Error(no='3_12_002', objectInfo=[record.objectInfo])
