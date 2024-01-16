from model import Person
from error import Error
import datetime
def process(record: Person):
    if (record.outInfo and record.objectInfo) is None:
        return
        # 1111-17-脱贫人口“是否已外出务工”选择为否，但务工结束时间为空或当前时间以后
    last=len(record.outInfo)-1
    Falg=0
    if record.outInfo[last]['结束时间']=='':
        Falg=1
    else:
        end_time = int(float(record.outInfo[-1]['结束时间'][0:4] + record.outInfo[-1]['结束时间'][5:-1]))
        now=int(str(datetime.date.today())[:7].replace('-',''))
        if now<end_time:
            Falg=1
    if record.objectInfo['户类型'] == '脱贫户' and record.outInfo[last]['是否已务工']=='否' and\
            Falg :
        raise Error(no='1111_17', outInfo=[record.outInfo[last]])




