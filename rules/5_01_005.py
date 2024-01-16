from model import Person
from error import Error
import pandas as pd
'''
5_01_005_203-已外出务工的脱贫人口务工地点未填写到县级（务工监测）
5_01_005_204-已外出务工的脱贫人口务工地点未填写到县级（基础信息务工地点）
'''
def process(record: Person):
    process203(record)
    process204(record)


def process203(record: Person):
    result = []
    if record.outInfo is None:
        return
    for i in record.outInfo:
        if i.get("户类型") == "脱贫户" and i.get("务工所在县") == '':
            result.append(i)
    if len(result) > 0:
        raise Error(no='5_01_005_203', msg='规则序号203', outInfo=result)


def process204(record: Person):
    if record.outInfo is None or record.objectInfo is None:
        return
    if ("县" not in record.objectInfo.get("务工所在地") and "区" not in record.objectInfo.get("务工所在地")) and record.objectInfo.get("户类型") == "脱贫户":
        raise Error(no='5_01_005_204', msg='规则序号204', objectInfo=[record.objectInfo], outInfo=record.outInfo)





