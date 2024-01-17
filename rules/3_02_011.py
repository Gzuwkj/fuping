from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["与户主关系"] == "户主":
        hoster = []
        for member in record.family.member:
            if member.objectInfo is None:
                continue
            hoster.append(member.family.host.idCard)
        hoster = list(set(hoster))
        if len(hoster) > 1:
            raise Error(no='3_02_011', objectInfo=[record.objectInfo])
