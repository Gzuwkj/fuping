# -*- coding: utf-8 -*-
from datetime import datetime

from model import Person
from error import Error
from typing import Dict, List

id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.objectInfo is None or record.family is None:
        return
    flag = 0
    for member in record.family.member:
        if member.objectInfo:
            medical_insurance = member.objectInfo.get("是否参加城乡居民基本养老保险")

            if medical_insurance is None:
               flag = 1
    if flag == 1:
        raise Error(no='2_15_001', objectInfo=[record.objectInfo],
                    msg="监测对象家庭成员是否参加大病保险为空")



