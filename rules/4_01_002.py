from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["健康状况"] == "残疾":
        if record.objectInfo["证件类型"] != "残疾人证":
            raise Error(no='4_01_002', objectInfo=[record.objectInfo])
