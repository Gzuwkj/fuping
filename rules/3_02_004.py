# -*- coding: utf-8 -*-
from datetime import datetime

from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime

id2record: Dict[str, List[Person]] = {}

def process(record: Person):
    if record.objectInfo is not None:
        # Check 3_02_004
        if record.objectInfo.get("户类型") == "脱贫户" and record.objectInfo.get("耕地面积（亩）") == '':
            raise Error(no='3_02_004', objectInfo=[record.objectInfo], msg="脱贫户耕地面积为空")




