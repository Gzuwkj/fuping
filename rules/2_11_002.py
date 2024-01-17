from model import Person
from error import Error
from typing import Dict, List
import os
from datetime import datetime
id2record: Dict[str, List[Person]] = {}
def timer(time):
    if time == '':
        return False
    else:
        if int(time[-2:]) >= 4 and int(time[:-2]) >= 2022:
            return True
        else:
            return False


def month_difference(date1, date2):
    if date1 == '' or date2 == '':
        return False
    else:
        dt1 = datetime.strptime(date1, '%Y%m')
        dt2 = datetime.strptime(date2, '%Y%m')
        delta = (dt2.year - dt1.year) * 12 + dt2.month - dt1.month
        if delta <= 2:
            return True
        else:
            return False
def process(record: Person):
    if record.objectInfo is None:
        return
    # 5_15_023-未消除风险识别时收入填写不合理（识别时工资性收入大于0小于100）
    if record.objectInfo['监测对象类别'] != '' and record.objectInfo['风险是否已消除'] == '是' and timer(record.objectInfo['消除监测时间']) and month_difference(record.objectInfo['消除监测时间'],record.objectInfo['识别监测时间']):
        raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                    msg='2_11_002-防止返贫监测对象从识别到风险消除时间低于6个月（2022年4月份以后消除风险）')





