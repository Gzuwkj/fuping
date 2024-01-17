from model import Person
from error import Error

def process(record: Person):
    if record.outInfo is None:
        return

    outInfoRecord = []
    for outInfo in record.outInfo:
        if outInfo.get('户类型') == '脱贫户' \
            and '长顺县' != outInfo.get('务工所在县') \
            and ('公益性岗位' in outInfo.get('就业渠道')
            or '帮扶车间' in outInfo.get('就业渠道')):
            outInfoRecord.append(outInfo)

    if len(outInfoRecord) != 0:
        raise Error(no='5_12_002', outInfo=outInfoRecord
                        , msg='县外务工的防止返贫监测对象人口填写了"就业渠道"中的"公益性岗位"和"帮扶车间"')

