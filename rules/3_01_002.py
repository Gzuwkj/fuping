# -*- coding: utf-8 -*-
from datetime import datetime

from model import Person
from error import Error
from typing import Dict, List

id2record: Dict[str, List[Person]] = {}

def process(record: Person):
    if record.objectInfo:
        education = record.objectInfo.get("文化程度")
        in_school_status = record.objectInfo.get("在校生状况")
        reason_for_not_attending_school = record.objectInfo.get("义务教育阶段未上学原因")
        household_type = record.objectInfo.get("户类型")
        if household_type == "脱贫户" and education is None and in_school_status is None and reason_for_not_attending_school is None:
            raise Error(no='3_01_002', objectInfo=[record.objectInfo],
                        msg="脱贫人口文化程度和在校生状况和失学原因同时为空")
