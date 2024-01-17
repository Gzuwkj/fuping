# -*- coding: utf-8 -*-
from datetime import datetime

from model import Person
from error import Error
from typing import Dict, List

id2record: Dict[str, List[Person]] = {}


def calculate_age(birthdate: str) -> int:
    today = datetime.today()
    birth_date = datetime.strptime(str(int(float(birthdate))), "%Y%m%d")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


def process(record: Person):
    if record.objectInfo is None:
        return

    age_field = '年龄'  # 请将这个字段替换为实际的字段名称
    labor_ability_field = '劳动技能'  # 请将这个字段替换为实际的字段名称
    household_type_field = '户类型'  # 请将这个字段替换为实际的字段名称
    person_id_field = '人编号'  # 请将这个字段替换为实际的字段名称
    birthdate_field = '出生日期'  # 请将这个字段替换为实际的字段名称

    age = record.objectInfo.get(age_field, None)
    labor_ability = record.objectInfo.get(labor_ability_field, None)
    household_type = record.objectInfo.get(household_type_field, None)
    person_id = record.objectInfo.get(person_id_field, None)
    birthdate = record.objectInfo.get(birthdate_field, None)

    if birthdate:
        calculated_age = calculate_age(birthdate)
        record.objectInfo[age_field] = calculated_age
        age = calculated_age

    if (
            age is not None and isinstance(age, int) and age >= 60
            and household_type == '脱贫户'
            and labor_ability in ('普通劳动力', '技能劳动力', '丧失劳动力')
    ):
        raise Error(no='2_12_017', objectInfo=[record.objectInfo])
