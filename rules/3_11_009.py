from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["风险是否已消除"] == "是":
        if record.objectInfo["是否有家庭成员未参加城乡居民（职工）基本医疗保险"] == "是":
            if record.objectInfo["健康帮扶"] == "" and record.objectInfo["社会帮扶"] == "":
                raise Error(no="3_11_009", objectInfo=[record.objectInfo])
