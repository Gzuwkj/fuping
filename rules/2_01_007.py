from model import Person
from error import Error
from typing import Dict, List



def process(record: Person):
    if record.objectInfo is None:
        return
    if len(str(record.objectInfo.get('是否参加城乡居民基本养老保险')).strip()) == 0 and str(record.objectInfo.get('户类型')) == '脱贫户':
        raise Error(no='2_01_007', objectInfo=[record.objectInfo])
