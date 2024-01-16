from model import Person
from error import Error

def process(record: Person):
    if (record.objectInfo and record.outInfo)is None:
        return
        # 1111_12-务工就业脱贫人口（含监测对象）月收入低于400元
    if int(float(record.outInfo[-1]["务工月收入"]))<400:
        raise Error(no='1111_12', objectInfo=[record.objectInfo])
