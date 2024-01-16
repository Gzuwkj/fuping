from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["风险是否已消除"] == "是":
        if record.objectInfo["是否解决安全饮用水"] == "是":
            if record.objectInfo["饮水安全保障"] == "":
                raise Error(no="3_11_008", objectInfo=[record.objectInfo])
