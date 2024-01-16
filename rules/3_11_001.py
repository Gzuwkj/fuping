from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.family.host is None:
        raise Error(no='3_11_001', objectInfo=[record.objectInfo])
