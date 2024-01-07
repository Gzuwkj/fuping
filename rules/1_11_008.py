from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["风险是否已消除"] == "是":
        for member in record.family.member:
            if member.objectInfo is None:
                continue
            if member.objectInfo["是否参加城乡居民基本医疗保险"] != "是":
                raise Error(no='1_11_008', objectInfo=[record.objectInfo])
