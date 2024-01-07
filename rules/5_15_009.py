from model import Person
from error import Error
import pandas as pd

def process(record: Person):

    if record.outInfo is None:
        return

    for outInfo in record.outInfo:
        if outInfo.get('户类型') == '脱贫户' \
            and '外出务工' in outInfo.get('就业渠道') \
            and len(outInfo.get('监测对象类别')) ==0\
            and (len(outInfo.get('所属行业')) == 0
                 or len(outInfo.get('务工企业名称')) == 0) :

            raise Error(no='5_15_009', outInfo=record.outInfo
                        , msg='监测对象人口务工监测有计划外出务工未填写务工需求')