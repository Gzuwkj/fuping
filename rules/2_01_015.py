from model import Person
import pandas as pd
from error import Error

'''
2_01_015-已外出务工或计划外出务工的脱贫人口无（含丧失）劳动能力<务工就业的脱贫人口（含监测对象）非劳动力或弱半劳动力>
'''
def process(record: Person):
    if record.objectInfo is None:
        return


    if (record.objectInfo.get("户类型") == "脱贫户" and record.objectInfo.get("劳动技能") in ["无劳动力", "丧失劳动力", "弱劳动力或半劳动力"]):
        if record.outInfo is not None or record.previewInfo is not None:
            raise Error(no='2_01_015', objectInfo=[record.objectInfo], outInfo=record.outInfo, previewInfo=record.previewInfo)




