from model import Person
from error import Error
import pandas as pd

'''
4_12_001-已外出务工的防止返贫监测对象人口务工地点未填写到县级（务工监测）
'''


def process(record: Person):
    process202(record)
    process206(record)


def process202(record: Person):
    result = []
    if record.outInfo is None:
        return
    for i in record.outInfo:
        if i.get("监测对象类别") != "" and i.get("务工所在县") == '':
            result.append(i)
    if len(result) > 0:
        raise Error(no='4_12_001_202', outInfo=result)


def process206(record: Person):
    outInfo_result = []
    previewInfo_result = []
    if record.outInfo is None:
        return
    for i in record.outInfo:
        if i.get("务工所在县") == '':
            outInfo_result.append(i)

    if record.previewInfo is None:
        return
    for j in record.previewInfo:
        if j.get("计划务工所在县") == '':
            previewInfo_result.append(j)
    if len(outInfo_result) > 0 or len(previewInfo_result) > 0:
        raise Error(no='4_12_001_206', outInfo=outInfo_result, previewInfo=previewInfo_result)
