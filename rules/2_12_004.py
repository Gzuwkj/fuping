# -*- coding: utf-8 -*-
from model import Person
from error import Error
from typing import Dict, List

id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.objectInfo is None or record.outInfo is None or record.previewInfo is None:
        return

    category_field = '监测对象类别'  # 请将这个字段替换为实际的字段名称
    work_status_field = '是否已务工'  # 请将这个字段替换为实际的字段名称
    plan_work_status_field = '是否计划外出务工'  # 请将这个字段替换为实际的字段名称
    labor_ability_field = '劳动技能'  # 请将这个字段替换为实际的字段名称
    person_id_field = '人编号'  # 请将这个字段替换为实际的字段名称

    category = record.objectInfo.get(category_field, None)
    #
    # if category is not None and category != '':
    person_id = record.objectInfo.get(person_id_field, None)
    errors = []
    if person_id is not None:
        if (
                record.outInfo.get(person_id_field, None) == person_id
                and record.outInfo.get(work_status_field, None) == '是'
                and record.outInfo.get(labor_ability_field, None) in (None, '丧失劳动力', '无劳动力')
        ) or (
                record.previewInfo.get(person_id_field, None) == person_id
                and record.previewInfo.get(plan_work_status_field, None) == '是'
                and record.previewInfo.get(labor_ability_field, None) in (None, '丧失劳动力', '无劳动力')):
            raise Error(no='2_12_004', objectInfo=[record.objectInfo], outInfo=[record.outInfo], previewInfo=[record.previewInfo], msg="已外出务工或计划外出务工防止返贫监测对象人口无（含丧失）劳动能力")
