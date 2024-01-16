from model import Person
from error import Error
from typing import Dict, List



def process(record: Person):
    if record.objectInfo is None:
        return
    numbers = record.objectInfo["证件号码"]
    if numbers[18:20]=="41" or numbers[18:20]=="42":
        if record.objectInfo["劳动技能"]=="普通劳动力":
            raise Error(no="4_01_007", objectInfo=[record.objectInfo])


