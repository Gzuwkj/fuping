from model import Person
from error import Error
from typing import Dict, List
import os
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["户类型"] == "脱贫户":
        hoster = []
        place = []
        for member in record.family.member:
            if member.objectInfo is None:
                continue
            if member.objectInfo['家庭成员联系电话'] not in hoster and member.objectInfo['家庭成员联系电话'] != '':
                hoster.append(member.objectInfo['家庭成员联系电话'])
                place.append(member.objectInfo['务工所在地'])
            else:
                for i in range(len(hoster)):
                    if hoster[i] == member.objectInfo['家庭成员联系电话']:
                        if place[i] != member.objectInfo['务工所在地']:
                            raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                                        msg='5_15_021-同户务工监测家庭成员务工所在区县不同但登记的联系电话号码一致')

