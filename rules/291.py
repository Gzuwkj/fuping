from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}


# 监测对象家庭成员中有义务教育阶段适龄儿童少年失学辍学但未享受义务教育保障
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['是否义务教育阶段适龄儿童少年失学辍学'] == '是':
        if record.objectInfo['义务教育保障'] == '':
            raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                        msg='监测对象家庭成员中有义务教育阶段适龄儿童少年失学辍学但未享受义务教育保障')
