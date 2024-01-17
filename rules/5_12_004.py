from model import Person
from error import Error
import pandas as pd
import datetime

def getAge(idcard):
    birth = idcard[6:10]
    age = datetime.date.today().year - int(birth)
    return age

def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get('户类型') == '脱贫户' \
        and getAge(record.objectInfo.get('证件号码')) < 16 :

        if record.outInfo is None:
            return

        outInfoRecord = []
        for outInfo in record.outInfo:
            if '公益岗位' in outInfo.get('就业渠道'):
                outInfoRecord.append(outInfo)

        if len(outInfoRecord) != 0:
            raise Error(no='5_12_004', objectInfo=[record.objectInfo], outInfo=outInfoRecord
                    , msg='16岁以下防止返贫监测对象人口参加“公益性岗位”')


