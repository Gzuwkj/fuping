# -*- coding: utf-8 -*-
from datetime import datetime

from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime

id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.outInfo is not None:
        out_info = record.outInfo
        is_working = out_info.get("是否已务工")
        if is_working is None:
            raise Error(no='3_01_009', outInfo=[out_info])

