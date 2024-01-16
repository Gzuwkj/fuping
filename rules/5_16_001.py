from model import Person
import pandas as pd
from error import Error

'''
5_16_001-目前务工防止返贫监测对象人口填写的务工月收入收入大于30000元或者小于100元
'''


result = []
def process(record: Person):
    if record.outInfo is None:
        return


    for i in record.outInfo:
        yueshouru = i.get("务工月收入")
        if not isinstance(yueshouru, (float, int)):
            try:
                yueshouru = float(yueshouru)
            except:
                raise Error(no='5_16_001', outInfo=record.outInfo)

        if i.get("监测对象类别") != "" and (yueshouru > 30000 or yueshouru < 100):
            result.append(i)
    raise Error(no='5_16_001', outInfo=result)

