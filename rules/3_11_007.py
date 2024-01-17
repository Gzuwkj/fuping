from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["风险是否已消除"] == "是":
        if record.objectInfo["是否义务教育阶段适龄儿童少年失学辍学"] == "是":
            if record.objectInfo["义务教育保障"] == "":
                raise Error(no="3_11_007", objectInfo=[record.objectInfo])
