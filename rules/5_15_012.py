from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}

def process(record: Person):
    if record.objectInfo is None:
        return
    # 5_15_023-未消除风险识别时收入填写不合理（识别时工资性收入大于0小于100）
    if record.objectInfo['教育帮扶'] == '雨露计划' and record.objectInfo['在校生状况'] not in ['中职一年级','中职二年级','中职三年级','高职高专一年级','高职高专二年级','高职高专三年级']:
        raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                    msg='5_15_012-监测对象人口2023年享受雨露计划职业教育补助人员但该人员不是中高职学生')






