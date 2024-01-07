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

    medical_insurance_resident = record.objectInfo.get("是否参加大病保险")
    medical_insurance_worker = record.objectInfo.get("是否参加城乡居民基本医疗保险")

    if medical_insurance_resident == "否" or medical_insurance_worker == "否":
        raise Error(no='2_12_016', objectInfo=[record.objectInfo],
                    msg="防止返贫监测人口医疗未保障")

