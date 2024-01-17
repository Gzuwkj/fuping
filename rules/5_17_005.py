from model import Person
import pandas as pd
from error import Error
from datetime import datetime
'''5_17_005-脱贫人口技师、高职高专、本科及研究生及以上小于18岁'''
def calculate_age(id_card):
    # 假设身份证号码格式为18位
    birth_date_str = id_card[6:14]  # 截取身份证号码中的出生日期部分
    birth_date = datetime.strptime(birth_date_str, "%Y%m%d")

    # 获取当前日期
    current_date = datetime.now()

    # 计算年龄
    age = current_date.year - birth_date.year - (
                (current_date.month, current_date.day) < (birth_date.month, birth_date.day))

    return age

def process(record: Person):
    if record.objectInfo is None:
        return
    age = calculate_age(record.idCard)
    if age < 18 and record.objectInfo.get("户类型") == "脱贫户" and record.objectInfo.get("文化程度") in ["技师", "高职高专", "本科及研究生及以上"]:
        raise Error(no='5_17_005', objectInfo=[record.objectInfo])
