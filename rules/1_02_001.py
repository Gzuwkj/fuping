from model import Person
from error import Error
from typing import Dict, List


'''
规则：脱贫户住危房但未纳入监测对象
完成！！！
'''


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo.get('户类型') == '脱贫户' and record.objectInfo.get('是否危房户') == '是':
        if len(str(record.objectInfo.get('监测对象类别')).strip()) == 0:
            raise Error(no='1_02_001', objectInfo=[record.objectInfo])

