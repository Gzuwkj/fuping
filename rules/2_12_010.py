# -*- coding: utf-8 -*-
from datetime import datetime

from model import Person
from error import Error
from typing import Dict, List

id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.objectInfo is None or record.family is None:
        return

    for member in record.family.member:
        if member.objectInfo:
            medical_insurance = member.objectInfo.get("是否参加大病保险")

            if medical_insurance is None:
                raise Error(no='2_12_010', objectInfo=[record.objectInfo, member.objectInfo], msg="监测对象家庭成员是否参加大病保险为空")


