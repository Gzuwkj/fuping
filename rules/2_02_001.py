# -*- coding: utf-8 -*-
from typing import List, Dict, Optional
from model import Person
from error import Error

id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get("户类型") in ["脱贫户", None] and record.objectInfo.get("与户主关系") == "户主":
        family_head_gender = record.objectInfo.get("性别")
        spouse_gender = None

        if record.family and len(record.family.member) > 1:
            # Find the spouse in the family
            for member in record.family.member:
                if member.objectInfo:
                    if member.objectInfo.get("与户主关系") == "配偶":
                        spouse_gender = member.objectInfo.get("性别")
                        break

        if family_head_gender and spouse_gender and family_head_gender == spouse_gender:
            raise Error(no='2_02_001', objectInfo=[record.objectInfo], msg="脱贫户主与配偶同性别")
