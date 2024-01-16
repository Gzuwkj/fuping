# from model import Person
# from error import Error
#
# def process(record: Person):
#     if record.objectInfo is None:
#         return
#         # 1111_4-2021年以来识别的防返贫监测对象享受搬迁措施
#     time=0
#     if record.objectInfo['识别监测时间'] != '':
#         time = 0
#         if int(float(record.objectInfo['识别监测时间'][:4])) >= 2021:
#             time = 1
#     if record.objectInfo['监测对象类别'] != '' and record.objectInfo['户类型'] == '脱贫户' \
#             and record.objectInfo['搬迁'] == '搬迁' and time:
#         raise Error(no='1111_4', objectInfo=[record.objectInfo])




from model import Person
from error import Error
from typing import Dict, List

def process(record: Person):
    if record.objectInfo is None:
        return