from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    status = str(record.objectInfo.get('是否参加大病保险')).strip()
    if status == '否' or len(status) == 0:
        if len(str(record.objectInfo.get('监测对象类别'))) == 0:
            raise Error(no='1_02_003', objectInfo=[record.objectInfo])



