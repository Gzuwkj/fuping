# -*- coding: utf-8 -*-
from typing import List, Dict, Optional
from model import Person
from error import Error

id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.objectInfo is None:
        return
    category = record.objectInfo.get("监测对象类别")
    if category != '':
        if record.objectInfo.get("与户主关系") == "户主":
            family_head_gender = record.objectInfo.get("gender")
            spouse_gender = None

            if record.family and len(record.family.member) > 1:
                # Find the spouse in the family
                for member in record.family.member:
                    if member.objectInfo:
                        if member.objectInfo.get("与户主关系") == "配偶":
                            spouse_gender = member.objectInfo.get("gender")
                            break

            if family_head_gender and spouse_gender and family_head_gender == spouse_gender:
                raise Error(no='2_11_003', objectInfo=[record.objectInfo], msg="监测对象户主与配偶同性别")
