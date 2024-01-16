from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["户类型"] == "脱贫户":
        try:
            dist = float(record.objectInfo["与村主干路距离"])
        except:
            raise Error(no='3_02_013', objectInfo=[record.objectInfo])
