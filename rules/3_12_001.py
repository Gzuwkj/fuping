from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.outInfo is None:
        return
    for idx, out in enumerate(record.outInfo):
        if out["开始时间"] == "":
            raise Error(no='3_12_002', objectInfo=[record.outInfo[idx]])
