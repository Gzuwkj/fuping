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
    if record.outInfo is None:
        return

    outInfoRecord = []
    for outInfo in record.outInfo:
        if record.objectInfo.get('户类型') == '脱贫户' \
                and '公益岗位' in outInfo.get('就业渠道') \
                and getAge(record.objectInfo.get('证件号码')) >= 70:
            outInfoRecord.append(outInfo)

    if len(outInfoRecord) != 0:
        raise Error(no='5_01_006', objectInfo=[record.objectInfo], outInfo=outInfoRecord
                        , msg='70岁及以上脱贫人口参加公益性岗位')


