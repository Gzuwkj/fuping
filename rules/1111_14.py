from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime
import os

# 1111_14-16（含）-60周岁（不含）健康监测对象人口劳动能力为半劳弱劳动力
id2record: Dict[str, List[Person]] = {}


def calculate_age(birthdate):
    # 将字符串类型的出生日期转换为datetime对象
    birth_date = datetime.strptime(birthdate, "%Y%m%d")

    # 获取当前日期
    current_date = datetime.now()

    # 计算年龄
    age = current_date.year - birth_date.year - (
            (current_date.month, current_date.day) < (birth_date.month, birth_date.day))

    return age


def process(record: Person):
    birthdate = record.idCard[6:14]
    age = calculate_age(birthdate)
    if record.objectInfo is None:
        return
    if 14 <= age < 60 and record.objectInfo['健康状况'] == '健康' and \
            record.objectInfo['监测对象类别'] != '' and record.objectInfo['在校生状况'] == '':
        if record.objectInfo['劳动技能'] == '弱劳动力或半劳动力' or record.objectInfo['劳动技能'] == '无劳动力':
            raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                        msg='1111_14-16（含）-60周岁（不含）健康监测对象人口劳动能力为半劳弱劳动力')
