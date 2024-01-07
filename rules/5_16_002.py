from model import Person
import pandas as pd
from error import Error
'''5_16_002-目前务工脱贫人口填写的务工月收入收入大于30000元或者小于100元'''

def process(record: Person):
    if record.outInfo is None or record.objectInfo is None:
        return


    for i in record.outInfo:
        yueshouru = i.get("务工月收入")
        if not isinstance(yueshouru, (float, int)):
            try:
                yueshouru = float(yueshouru)
            except:
                raise Error(no='5_16_002', outInfo=record.outInfo)
                break

        if i.get("户类型") == "脱贫户" and (yueshouru > 30000 or yueshouru < 100):
            raise Error(no='5_16_002', outInfo=record.outInfo)
            break


