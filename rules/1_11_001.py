from model import Person
from error import Error
from typing import Dict, List

def process(record: Person):
    if record.objectInfo is None:
        return

    if len(str(record.objectInfo.get('监测对象类别')).strip()) != 0:
        if len(str(record.objectInfo.get('致贫/返贫风险1')).strip()) == 0:
            raise Error(no='1_11_001', objectInfo=[record.objectInfo])
