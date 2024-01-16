from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo.get('是否危房户') == '是':
        if len(str(record.objectInfo.get('监测对象类别')).strip()) == 0:
            raise Error(no='1_02_001', objectInfo=[record.objectInfo])

