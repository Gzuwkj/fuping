# -*- coding: utf-8 -*-
from datetime import datetime

from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime

id2record: Dict[str, List[Person]] = {}

def process(record: Person):
    if record.objectInfo is not None:
        # Check 2_02_002
        if record.objectInfo.get("户类型") == "脱贫户" and (record.objectInfo.get("是否通生活用电") == "否" or record.objectInfo.get("是否通生活用电") == ""):
            raise Error(no='2_02_002', objectInfo=[record.objectInfo], msg="脱贫户未通生活用电")




