# -*- coding: utf-8 -*-
from datetime import datetime

from model import Person
from error import Error
from typing import Dict, List

id2record: Dict[str, List[Person]] = {}

def process(record: Person):
    if record.objectInfo:
        household_type = record.objectInfo.get("户类型")
        employment_time = record.objectInfo.get("公益性岗位(月数)")
        public_service_position = record.objectInfo.get("公益性岗位")

        if household_type == "脱贫户" and employment_time is not None and public_service_position is None:
            raise Error(no='3_01_005', objectInfo=[record.objectInfo],
                        msg="脱贫人员填写了聘用时间但未填写聘用公益性岗位")

