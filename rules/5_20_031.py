from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}


# 脱贫人口劳动能力为技能劳动力但未务工就业
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['户类型'] == '脱贫户':
        if record.objectInfo['劳动技能'] == '技能劳动力':
            if record.outInfo is None:
                raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo], outInfo=record.outInfo,
                            msg='脱贫人口劳动能力为技能劳动力但未务工就业')
