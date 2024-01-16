# -*- coding: utf-8 -*-
from datetime import datetime

from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime

id2record: Dict[str, List[Person]] = {}

def process(record: Person):
    if record.family is not None and record.family.host is not None:
        family = record.family
        if family.host.objectInfo is not None and family.host.objectInfo.get("户类型") != "脱贫户":
            public_work_count = 0

            for member in family.member:
                if member.objectInfo is not None and member.objectInfo.get("公益性岗位"):
                    public_work_count += 1

                if public_work_count > 3:
                    raise Error(no='3_01_011', objectInfo=[family.host.objectInfo],
                                msg="监测对象人口登记3种及以上公益性岗位")


