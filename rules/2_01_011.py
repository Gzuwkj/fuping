from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime

'''
规则：16岁（不含）以下脱贫人口劳动能力不是无劳动能力
完成！！！！
'''


def process(record: Person):
    if record.objectInfo is None:
        return
    if str(record.objectInfo.get('户类型')).strip() == '脱贫户':
        birthDate = datetime.strptime(record.idCard.strip()[6:14], "%Y%m%d")
        currentDate = datetime.now()
        age = currentDate.year - birthDate.year - ((currentDate.month, currentDate.day) < (birthDate.month, birthDate.day))
        if age < 16 and record.objectInfo.get('劳动技能') != '无劳动力':
            raise Error(no='2_01_011', objectInfo=[record.objectInfo])
