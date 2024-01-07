from model import Person
from error import Error

def process(record: Person):
    # 1111_08-脱贫人口2020年务工至今未回人员名单
    if (record.outInfo and record.objectInfo) is None:
        return
    last = len(record.outInfo) - 1
    if record.objectInfo['户类型'] == '脱贫户' and record.outInfo[last]['开始时间'][:4] == '2020' and \
            record.outInfo[last]['结束时间'] == '':
        raise Error(no='1111_08', outInfo=record.outInfo)