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

    for outInfo in record.outInfo:
        if record.objectInfo.get('户类型') == '脱贫户' \
                and '公益岗位' in record.objectInfo.get('就业渠道（易地搬迁后扶使用）') \
                and outInfo.get('就业渠道') == '公益岗位'\
                and getAge(record.objectInfo.get('证件号码')) >= 70:
            raise Error(no='5_01_006', objectInfo=[record.objectInfo], outInfo=[record.outInfo]
                        , msg='70岁及以上脱贫人口参加公益性岗位')


