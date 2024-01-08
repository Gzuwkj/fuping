from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["户类型"] == "脱贫户":
        if len(record.objectInfo["是否危房户"]) == 0:
            raise Error(no='3_02_009', objectInfo=[record.objectInfo])
