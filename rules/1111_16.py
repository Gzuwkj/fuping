from model import Person
from error import Error

def process(record: Person):
    # 1111-16-防止返贫监测对象人口“是否已外出务工”选择为否，但务工结束时间为空或当前时间以后
    if (record.outInfo and record.objectInfo) is None:
        return
    last = len(record.outInfo) - 1
    if record.objectInfo['监测对象类别'] != '' and record.outInfo[last]['是否已务工'] == '否' and \
            record.outInfo[last]['结束时间'] == '':
        raise Error(no='1111_16', outInfo=record.outInfo)
