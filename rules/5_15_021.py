from model import Person
from error import Error
from typing import Dict, List
import os
def check_unique(x):
  return len(x) == len(set(x))
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["户类型"] == "脱贫户":
        hoster = []
        for member in record.family.member:
            if member.objectInfo is None:
                continue
            if member.objectInfo['家庭成员联系电话'] != '':
                hoster.append(member.objectInfo['家庭成员联系电话'])
        hoster = list(set(hoster))
        if check_unique(hoster):
            raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],msg='5_15_021-同户务工监测家庭成员务工所在区县不同但登记的联系电话号码一致')
