from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return
        # 1111_12-务工就业脱贫人口（含监测对象）月收入低于400元
    if record.objectInfo['务工所在地'] != '' and record.objectInfo['监测对象类别'] != '' and \
                record.objectInfo['户类型'] == '脱贫户' and float(record.objectInfo['年收入（元）']) < 4800:
        raise Error(no='1111_12', objectInfo=[record.objectInfo])
