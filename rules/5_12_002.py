from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime
import os


def sort_by_time(dictionary):
    # 提取时间字段并转换为datetime对象
    time_str = dictionary["开始时间"]
    time_object = datetime.strptime(time_str, "%Y年%m月")
    return time_object


def parse_date(date_str):
    return datetime.strptime(date_str, "%Y年%m月")


# 按时间字段排序

# 外出务工的脱贫人口务工开始时间早于上次务工结束时间
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.outInfo is not None:
        if record.objectInfo['户类型'] == '脱贫户':
            if record.outInfo.__len__() >= 2:
                sortTimeOutInfo = sorted(record.outInfo, key=sort_by_time)
                previous_end_time = parse_date(sortTimeOutInfo[0]["结束时间"])
                for i in range(1, len(sortTimeOutInfo)):
                    start_time = parse_date(sortTimeOutInfo[i]["开始时间"])
                    if start_time <= previous_end_time:
                        raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                                    outInfo=[record.outInfo[-1]],
                                    msg='外出务工的脱贫人口务工开始时间早于上次务工结束时间')
