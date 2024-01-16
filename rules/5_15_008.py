from model import Person
from error import Error
import pandas as pd

def process(record: Person):
    if record.outInfo is None:
        return

    outInfoRecord = []
    for outInfo in record.outInfo:
        if outInfo.get('户类型') == '脱贫户' \
            and '外出务工' in outInfo.get('就业渠道') \
            and (len(outInfo.get('所属行业')) == 0
                 or len(outInfo.get('务工企业名称')) == 0) :
            outInfoRecord.append(outInfo)

    if len(outInfoRecord) != 0:
        raise Error(no='5_15_008', outInfo=outInfoRecord
                        , msg='脱贫人口务工监测有计划外出务工未填写务工需求')

