# -*- coding: utf-8 -*-
from datetime import datetime

from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime

id2record: Dict[str, List[Person]] = {}
def calculate_age(birthdate: str) -> int:
    birthdate = datetime.strptime(str(int(float(birthdate))), "%Y%m%d")
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def process(record: Person):
    if record.objectInfo is None or record.family is None:
        return
    birthdate = record.objectInfo.get("出生日期")
    labor_skill = record.objectInfo.get("劳动技能")
    category = record.objectInfo.get("监测对象类别")
    if category != '' and birthdate and labor_skill:
        age = calculate_age(birthdate)

        if age < 16 and labor_skill != "无劳动力":
            raise Error(no='2_12_014', objectInfo=[record.objectInfo],
                        msg="16岁以下监测对象人口劳动能力不是无劳动力")
