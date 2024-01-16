# -*- coding: utf-8 -*-
from typing import List, Dict, Optional
from model import Person
from error import Error

id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.objectInfo is None:
        return

        # Rule 2_11_004: 监测对象致贫返贫风险类型为其他但未填写备注
    risk_fields = ["致贫/返贫风险1", "致贫/返贫风险2", "致贫/返贫风险3", "致贫/返贫风险4", "致贫/返贫风险5"]

    for field in risk_fields:
        risk_type = record.objectInfo.get(field)
        risk_remark = record.objectInfo.get("其他备注")

        if risk_type == "其他" and not risk_remark:
            raise Error(no='2_11_004', objectInfo=[record.objectInfo])
