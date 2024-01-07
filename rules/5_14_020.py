from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}

def process(record: Person):
    if record.objectInfo is None:
        return
    # 5_15_023-未消除风险识别时收入填写不合理（识别时工资性收入大于0小于100）
    if record.objectInfo['监测对象类别'] != '' and record.objectInfo['水面面积'] == '':
        raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                    msg='5_14_020-监测对象水面面积为空')






