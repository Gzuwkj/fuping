from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}

def process(record: Person):
    if record.objectInfo is None:
        return
    # 5_15_023-未消除风险识别时收入填写不合理（识别时工资性收入大于0小于100）
    if record.objectInfo['户类型'] == '脱贫户' and (float(record.objectInfo['牧草地面积'])< 0 and float(record.objectInfo['牧草地面积'])>100):
        raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                    msg='5_14_005-脱贫户牧草地面积小于0或大于100亩')





