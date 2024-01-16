# -*- coding: utf-8 -*-
from typing import List, Dict, Optional
from model import Person,Family
from error import Error
from uuid import uuid4

id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.objectInfo is None:
        return

    # Rule 2_11_001: 防止返贫监测对象户返（致）贫风险为“因残”但家中无残疾人
    risk_fields = ["致贫/返贫风险1", "致贫/返贫风险2", "致贫/返贫风险3", "致贫/返贫风险4"]
    if any(
        record.objectInfo.get(risk_field) == "因残"
        and not has_disabled_person(record.family)
        for risk_field in risk_fields
    ):
        raise Error(no='2_11_001', objectInfo=[record.objectInfo])


def has_disabled_person(family: Family) -> bool:
    for member in family.member:
        if member.objectInfo.get("证件类型") == "残疾人证":
            return True
    return False
