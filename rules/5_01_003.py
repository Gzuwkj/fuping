from model import Person
from error import Error
import pandas as pd

def process(record: Person):
    if record.objectInfo is None:
        return

    strBuf = record.objectInfo.get('就业渠道（易地搬迁后扶使用）')
    if not pd.isna(strBuf) :
        if record.objectInfo.get('户类型') == '脱贫户' \
                and '公益性岗位' in record.objectInfo.get('就业渠道（易地搬迁后扶使用）')\
                and '帮扶车间' in record.objectInfo.get('就业渠道（易地搬迁后扶使用）'):
            raise Error(no='5_01_003', record=record
                        , msg='县外务工的脱贫人口填写了"就业渠道"中的"公益性岗位"和"帮扶车间"(务工月监测)')


    if record.outInfo is None:
        return

    for outInfo in record.outInfo:
        if outInfo.get('户类型') == '脱贫户' \
                and '公益性岗位' in outInfo.get('务工企业名称')\
                and '帮扶车间' in outInfo.get('就业渠道'):


            raise Error(no='5_01_003', record=record
                            , msg='县外务工的脱贫人口填写了"就业渠道"中的"公益性岗位"和"帮扶车间"(务工月监测)')

