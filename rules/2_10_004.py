from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return
        # 2_10_004-2021年以来公益岗位项目的建设内容为空
    time = 0
    if record.objectInfo['识别监测时间'] != '':
        time = 0
        if int(float(record.objectInfo['识别监测时间'][:4])) >= 2021:
            time = 1
    if record.objectInfo['公益性岗位'] == '' and time:
        raise Error(no='2_10_004', objectInfo=[record.objectInfo])