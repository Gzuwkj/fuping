# -*- coding: utf-8 -*-
from datetime import datetime

from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime

id2record: Dict[str, List[Person]] = {}



def process(record: Person):
    if record.objectInfo is not None and record.objectInfo.get("户类型") == "脱贫户":
        public_work_positions_str = record.objectInfo.get("公益性岗位", "")
        public_work_positions = public_work_positions_str.split(',')
        public_work_positions = [position.strip() for position in public_work_positions]
        unique_positions = set(public_work_positions)
        if len(unique_positions) > 1:
            raise Error(no='3_01_010', objectInfo=[record.objectInfo],
                        msg="脱贫人口登记3种及以上公益性岗位")