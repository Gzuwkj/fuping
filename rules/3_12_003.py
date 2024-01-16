from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["文化程度"] == "" and record.objectInfo["在校生状况"] == "" and record.objectInfo["义务教育阶段未上学原因"] == "":
        raise Error(no='3_12_003', objectInfo=[record.objectInfo])
