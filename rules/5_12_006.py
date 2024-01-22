from model import Person
import pandas as pd
from error import Error

'''
5_12_006-目前务工防止返贫监测对象人口未填写务工月收入、务工企业名称、所属行业、是否点对点输送和就业渠道(测用务工信息)
'''


def process(record: Person):
    if record.outInfo is None or record.objectInfo is None:
        return
    result = []
    for i in record.outInfo:
        if i.get("监测对象类别") != "" and any(
                not i.get(field) for field in ["务工月收入", "务工企业名称", "所属行业", "就业渠道", "是否点对点输送"]):
            result.append(i)
    if len(result) > 0:
        raise Error(no='5_12_006', outInfo=result)

