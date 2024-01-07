# -*- coding: utf-8 -*-
from datetime import datetime

from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime

id2record: Dict[str, List[Person]] = {}

def process(record: Person):
    if record.objectInfo is None or record.family is None:
        return

    medical_insurance_resident = record.objectInfo.get("是否参加城乡居民基本医疗保险")
    medical_insurance_worker = record.objectInfo.get("是否参加城镇职工基本医疗保险")

    if medical_insurance_resident == "是" and medical_insurance_worker == "是":
        raise Error(no='2_12_015', objectInfo=[record.objectInfo],
                    msg="防止返贫监测对象人口同时参加城乡居民和城镇职工基本医疗保险")

