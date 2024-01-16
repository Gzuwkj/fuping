from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return
        # 1_02_006-脱贫户2023年人均纯收入低于7300元但未纳入防止返贫监测对象户
    if int(float(record.objectInfo['人均纯收入（元）'])) < 7300 and \
            record.objectInfo['监测对象类别'] == '':
        raise Error(no='1_02_006', objectInfo=[record.objectInfo])

    # record.objectInfo['户类型'] == '脱贫户' and