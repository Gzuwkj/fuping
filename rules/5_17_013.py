from model import Person
from error import Error

def process(record: Person):
    # 5_17_013 - 防止防贫监测对象识别后家中无新增县外务工人员但措施登记了劳务输出
    if (record.outInfo and record.objectInfo ) is None or record.objectInfo['识别监测时间']=='':
        return
    start_time=int(float(record.outInfo[-1]['开始时间'][0:4]+record.outInfo[-1]['开始时间'][5:-1]))
    Flag=int(float(record.objectInfo['识别监测时间']))>start_time #如DF列“识别监测时间”大于务工月监测已外出务工表M列“开始时间”
    if record.objectInfo['监测对象类别'] != '' and record.objectInfo['就业帮扶'] == '劳务输出'and Flag:
        raise Error(no='5_17_013', outInfo=record.outInfo,objectInfo=[record.objectInfo])
