from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    public_job_help = str(record.objectInfo.get('就业帮扶'))
    if public_job_help != '':
        labour_skill = str(record.objectInfo.get('劳动技能'))
        if labour_skill == '无劳动能力' or labour_skill == '丧失劳动力':
            raise Error(no='5_15_006', objectInfo=[record.objectInfo])



