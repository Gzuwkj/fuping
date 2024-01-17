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
    if record.objectInfo['监测对象类别'] != '' and record.objectInfo['风险是否已消除'] == '否':
        for member in record.family.member:
            if member.objectInfo is None:
                continue
            if member.objectInfo['致贫/返贫风险1'] == '因务工就业不稳':
                i = i + 1
                if len(record.family.member) == i:
                    raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                                msg='5_15_014-未消除风险的监测对象致贫返贫风险为因务工就业不稳但家中人员均未登记务工信息')






