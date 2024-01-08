from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return
        # 3_02_002-脱贫户“是否解决安全饮用水”为空
    if record.objectInfo['户类型'] == '脱贫户' and record.objectInfo['是否解决安全饮用水'] == '':
        raise Error(no='3_02_002', objectInfo=[record.objectInfo])