# from model import Person
# from error import Error
# from typing import Dict, List
# # id2record: Dict[str, List[Person]] = {}
# from datetime import datetime
#
# def process(record: Person):
#     if record.objectInfo is None:
#         return
#     a = list(record.objectInfo['出生日期'][:-2])
#     a.insert(4, '-')
#     a.insert(7, '-')
#     str_i = ''.join(a)
#     if len(str_i)<10:
#         return
#     age = age_calc(str_i)
#     # 5_17_007-16(含)-22周岁(含)脱贫人口文化程度为小学及以下
#     if record.objectInfo['户类型'] == '脱贫户' and (record.objectInfo['文化程度'] == '小学' \
#            or record.objectInfo['文化程度'] == '文盲或半文盲' )\
#         and age <= 22 :
#         raise Error(no='5_17_007', objectInfo=[record.objectInfo])
# def age_calc(birth_date):
#     end_date=datetime.now().strftime('%Y-%m-%d')
#     end_date = datetime.strptime(end_date, '%Y-%m-%d')
#     # change the type of date to datetime
#     birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
#
#     # compute the difference of day, month and year
#     day_diff = end_date.day - birth_date.day
#     month_diff = end_date.month - birth_date.month
#     year_diff = end_date.year - birth_date.year
#
#     # compute age based on the diffference of day, month and year
#     if day_diff >= 0:
#         if month_diff >= 0:
#             years_old = year_diff
#         else:
#             years_old = year_diff - 1
#     else:
#         if month_diff >= 1:
#             years_old = year_diff
#         else:
#             years_old = year_diff - 1
#     return years_old

from model import Person
from error import Error

def process(record: Person):
    # 1111_08-脱贫人口2020年务工至今未回人员名单
    if (record.outInfo and record.objectInfo) is None:
        return