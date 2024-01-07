from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime
import os

id2record: Dict[str, List[Person]] = {}


# 16(含)-22周岁(含)含监测对象文化程度为小学及以下


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
    if record.objectInfo is None:
        return
    if record.objectInfo['文化程度'] == '小学' or record.objectInfo['文化程度'] == '文盲或半文盲':
        birthdate = record.idCard[6:14]
        age = calculate_age(birthdate)
        if 16 <= age <= 22:
            raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                        msg='16(含)-22周岁(含)含监测对象文化程度为小学及以下')
