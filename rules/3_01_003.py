from model import Person
from error import Error
from datetime import datetime
'''3_01_003-脱贫人口文化程度和在校生状况同时填报'''

def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get("户类型") == "脱贫户" and record.objectInfo.get("在校生状况") == "" and record.objectInfo.get("文化程度") == "":
        raise Error(no='3_01_003', objectInfo=[record.objectInfo])
