# -*- coding: utf-8 -*-
from model import Person
from error import Error
from typing import Dict, List

id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.objectInfo is None:
        return

    risk_fields = ['致贫/返贫风险1', '致贫/返贫风险2', '致贫/返贫风险3', '致贫/返贫风险4', '致贫/返贫风险5']
    natural_disaster_field = '因自然灾害子项'  # 请将这个字段替换为实际的字段名称
    category = record.objectInfo.get("监测对象类别")
    if category != '':
        risks = [record.objectInfo.get(field) for field in risk_fields]
        natural_disaster_type = record.objectInfo.get(natural_disaster_field, None)

        if '因自然灾害' in risks and natural_disaster_type is None:
            raise Error(no='2_11_005', objectInfo=[record.objectInfo])