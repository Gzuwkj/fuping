from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}

def process(record: Person):
    if record.objectInfo is None:
        return
    i = 0
    # 5_15_023-未消除风险识别时收入填写不合理（识别时工资性收入大于0小于100）
    if record.objectInfo['致贫/返贫风险1'] == '务工就业不稳':
        for member in record.family.member:
            if member.objectInfo is None:
                continue
            if member.objectInfo['劳动技能'] == '无劳动力' or member.objectInfo['劳动技能'] == '丧失劳动力':
                i = i + 1
                if len(record.family.member) == i:
                    raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                                msg='5_15_013-致贫返贫风险为因务工就业不稳家中人员均无（含丧失）劳动力（含自然减少）')







