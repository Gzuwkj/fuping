from model import Person
from error import Error
# from datetime import datetime
import datetime

def process(record: Person):
    # 1111-16-防止返贫监测对象人口“是否已外出务工”选择为否，但务工结束时间为空或当前时间以后
    if (record.outInfo and record.objectInfo) is None:
        return
    last = len(record.outInfo) - 1
    Falg = 0
    if record.outInfo[last]['结束时间'] == '':
        Falg = 1
    else:
        end_time = int(float(record.outInfo[-1]['结束时间'][0:4] + record.outInfo[-1]['结束时间'][5:-1]))
        now = int(str(datetime.date.today())[:7].replace('-', ''))
        if now < end_time:
            Falg = 1
    if record.objectInfo['监测对象类别'] != '' and record.outInfo[last]['是否已务工'] == '否' and \
            Falg:
        raise Error(no='1111_16', outInfo=[record.outInfo[last]])
