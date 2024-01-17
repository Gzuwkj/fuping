# -*- coding: utf-8 -*-
from model import Person
from error import Error
from typing import Dict, List

id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.objectInfo is None:
        return

    risk_fields = ['致贫/返贫风险1', '致贫/返贫风险2', '致贫/返贫风险3', '致贫/返贫风险4', '致贫/返贫风险5']
    labor_skill_field = '劳动技能'  # 请将这个字段替换为实际的字段名称
    category = record.objectInfo.get("监测对象类别")
    fengxian = record.objectInfo.get("风险是否已消除0")
    if category != '' and fengxian == "否":
        risks = [record.objectInfo.get(field) for field in risk_fields]
        labor_skill = record.objectInfo.get(labor_skill_field, None)

        if '因务工就业不稳' in risks and (labor_skill == '无劳动力' or labor_skill == '丧失劳动力'):
            raise Error(no='2_11_006', objectInfo=[record.objectInfo])