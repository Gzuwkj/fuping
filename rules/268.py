from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['就业帮扶'] != '' or record.objectInfo['公益性岗位'] != '':
        for index, member in enumerate(record.family.member):
            if member.outInfo is not None:
                break
            if index == record.family.member.__len__() - 1 and member.outInfo is None:
                raise Error(no='268', objectInfo=[record.objectInfo],
                            msg='1111_3-登记就业帮扶或公益性岗位但识别以来家中无人务工(务工月监测)')
