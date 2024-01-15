from model import Person
from error import Error

def process(record: Person):
    if (record.outInfo and record.objectInfo) is None:
        return
        # 1111-17-脱贫人口“是否已外出务工”选择为否，但务工结束时间为空或当前时间以后
    last=len(record.outInfo)-1
    if record.objectInfo['户类型'] == '脱贫户' and record.outInfo[last]['是否已务工']=='否' and\
            record.outInfo[last]['结束时间']=='' :
        raise Error(no='1111_17', outInfo=[record.outInfo[last]])




