from model import Person
from error import Error
from typing import Dict, List



def process(record: Person):
    if record.objectInfo is None:
        return
    if len(str(record.objectInfo.get('是否参加大病保险')).strip()) == 0 and str(record.objectInfo.get('户类型')) == '脱贫户':
        raise Error(no='2_01_006', objectInfo=[record.objectInfo])
