from model import Person
from error import Error
from typing import Dict, List
# id2record: Dict[str, List[Person]] = {}
from datetime import datetime
import os

def process(record: Person):
    if record.objectInfo is None:
        return
    # 5_15_023-未消除风险识别时收入填写不合理（识别时工资性收入大于0小于100）
    if record.objectInfo['监测对象类别'] != '' and record.objectInfo['否义务教育阶段适龄儿童少年失学辍学'] != '':
        raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                    msg='5_15_017-监测对象家庭成员义务教育适龄儿童不在校')






