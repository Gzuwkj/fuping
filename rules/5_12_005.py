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
        and len(record.objectInfo.get('监测对象类别')) != 0 \
        and float(getAge(record.objectInfo.get('证件号码'))) >= 70 :

        if record.outInfo is None:
            return

        outInfoRecord = []
        for outInfo in record.outInfo:
            if '公益岗位' in outInfo.get('就业渠道'):
                outInfoRecord.append(outInfo)

        if len(outInfoRecord) != 0:
            raise Error(no='5_12_005', objectInfo=[record.objectInfo], outInfo=outInfoRecord
                        , msg='70岁及以上防止返贫监测对象人口参加公益性岗位')




