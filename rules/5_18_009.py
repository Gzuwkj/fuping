from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime
import os

id2record: Dict[str, List[Person]] = {}


# 贵州乡村振兴云-防止返贫监测对象户当月及次月消除返（致）贫风险（不含自然消除）
def calculate_month_difference(date_str1, date_str2):
    # 将输入的年月字符串转换为datetime对象
    date1 = datetime.strptime(date_str1, "%Y%m")
    date2 = datetime.strptime(date_str2, "%Y%m")
    # 计算月份差异
    month_difference = (date2.year - date1.year) * 12 + date2.month - date1.month
    return month_difference


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['监测对象类别'] != '' and record.objectInfo['风险是否已消除'] == '是':
        if record.objectInfo['风险消除方式'] == '帮扶消除':
            if record.objectInfo['识别监测时间'] != '' and record.objectInfo['消除监测时间'] != '':
                if calculate_month_difference(record.objectInfo['识别监测时间'],
                                              record.objectInfo['消除监测时间']) <= 2:
                    raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                                msg='贵州乡村振兴云-防止返贫监测对象户当月及次月消除返（致）贫风险（不含自然消除）')
