from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return
    time = 0    # 1111_18-2023年以来识别的防止返贫监测户风险识别时人均纯收入高于20000元
    if record.objectInfo['识别监测时间'] != '':

        if int(float(record.objectInfo['识别监测时间'][:4])) >= 2023:
            time = 1
    if int(float(record.objectInfo['人均纯收入（元）'])) > 20000 and  time:
        raise Error(no='1111_18', objectInfo=[record.objectInfo])


    #record.objectInfo['监测对象类别'] != '' and \
        # record.objectInfo['户类型'] == '脱贫户' and