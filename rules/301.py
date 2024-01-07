from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}


# 脱贫户整户无劳动力但家中无享受最低生活保障政策人员
def process(record: Person):
    if record.objectInfo is None:
        return
    for index, member in enumerate(record.family.member):
        if member.objectInfo is not None:
            if member.objectInfo['劳动技能'] != '无劳动力' or member.objectInfo['最低生活保障金'] != '0.00':
                break
            if index == record.family.member.__len__():
                raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                            msg='脱贫户整户无劳动力但家中无享受最低生活保障政策人员')
