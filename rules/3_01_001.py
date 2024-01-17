# -*- coding: utf-8 -*-
from datetime import datetime

from model import Person
from error import Error
from typing import Dict, List

id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.family is not None and record.family.host is not None:
        relationship_with_host = record.objectInfo.get("与户主关系")
        if relationship_with_host is None:
            raise Error(no='3_01_001', objectInfo=[record.objectInfo],
                        msg="脱贫人口与户主关系为空")
