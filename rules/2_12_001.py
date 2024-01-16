# -*- coding: utf-8 -*-
from model import Person
from error import Error
from typing import Dict, List

id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.objectInfo is None:
        return

    labor_skill_field = '劳动技能'  # 请将这个字段替换为实际的字段名称
    labor_skill = record.objectInfo.get(labor_skill_field, None)

    if labor_skill is None or labor_skill == '':
        raise Error(no='2_12_001', objectInfo=[record.objectInfo])