from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    for m in record.family.member:
        public_welfare = str(m.objectInfo.get('公益性岗位'))
        if public_welfare != '':
            labour_skill = str(m.objectInfo.get('劳动技能'))
            if labour_skill == '无劳动能力' or labour_skill == '丧失劳动力':
                raise Error(no='5_15_006', objectInfo=[record.objectInfo])



