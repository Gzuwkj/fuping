from model import Person
from error import Error
from typing import Dict, List
# id2record: Dict[str, List[Person]] = {}
from datetime import datetime

def process(record: Person):
    if record.objectInfo is None:
        return

    # 5_15_023-未消除风险识别时收入填写不合理（识别时工资性收入大于0小于100）
    if record.objectInfo['风险是否已消除'] == '否' and  0<int(float(record.objectInfo['工资性收入']))<100 :
        raise Error(no='5_15_0023', objectInfo=[record.objectInfo])






