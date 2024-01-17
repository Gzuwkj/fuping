from model import Person
from error import Error
from typing import Dict, List
# id2record: Dict[str, List[Person]] = {}
import datetime
import os

def howOld(old):
    now = datetime.datetime(2024,9,1)
    birthday = datetime.datetime(int(old[6:10]),int(old[10:12]),int(old[12:14]))
    age = now.year -birthday.year - ((now.month,now.day) < (birthday.month,birthday.day))
    if age >= 6 and age <= 16:
        return True
    else:
        return False
def process(record: Person):
    if record.objectInfo is None:
        return
    # 5_15_023-未消除风险识别时收入填写不合理（识别时工资性收入大于0小于100）
    if record.objectInfo['监测对象类别'] != '' and howOld(record.objectInfo['证件号码']) and (record.objectInfo['在校生状况'] == '' and record.objectInfo['义务教育阶段未上学原因'] == ''):
        raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                    msg='5_15_017-监测对象家庭成员义务教育适龄儿童不在校')






