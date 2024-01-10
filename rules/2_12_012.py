# -*- coding: utf-8 -*-
from datetime import datetime

from model import Person
from error import Error
from typing import Dict, List

id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.objectInfo is None or record.family is None:
        return
    member = record.family.member
    if member.objectInfo:
        medical_insurance1 = member.objectInfo.get("是否参加城乡居民基本医疗保险")
        medical_insurance2 = member.objectInfo.get("是否参加城镇职工基本医疗保险")

        if medical_insurance1 is None and medical_insurance2 is None:
            raise Error(no='2_12_012', objectInfo=[record.objectInfo, member.objectInfo],
                        msg="监测对象家庭成员是否参加城乡居民（职工）基本医疗保险同时为空")



