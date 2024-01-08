from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime
import os

# 5_16_010-16岁以下（务工开始时间与出生年月相减）脱贫人口（含监测对象）有务工登记
id2record: Dict[str, List[Person]] = {}


def calculate_age(birthdate, beginTime):
    # 将字符串类型的出生日期转换为datetime对象
    current_date_str = beginTime
    birthdate_str = birthdate
    # 将字符串转换为 datetime 对象
    current_date = datetime.strptime(current_date_str, "%Y年%m月")
    birthdate = datetime.strptime(birthdate_str, "%Y%m%d")
    # 计算年龄
    age = current_date.year - birthdate.year - (
            (current_date.month, current_date.day) < (birthdate.month, birthdate.day))
    return age


def process(record: Person):
    birthdate = record.idCard[6:14]
    if record.objectInfo is None:
        return
    if record.outInfo is not None:
        beginTime = record.outInfo[0]['开始时间']
        age = calculate_age(birthdate, beginTime)
        if age < 16 and record.objectInfo['户类型'] == '脱贫户':
            raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                        outInfo=[record.outInfo[-1]],
                        msg='5_16_010-16岁以下（务工开始时间与出生年月相减）脱贫人口（含监测对象）有务工登记')
