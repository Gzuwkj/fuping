from model import Person
from error import Error

def process(record: Person):
    # 5_17_013 - 防止防贫监测对象识别后家中无新增县外务工人员但措施登记了劳务输出
    if (record.outInfo and record.objectInfo) is None:
        return
    if record.objectInfo['监测对象类别'] != '' and record.objectInfo['就业帮扶'] == '劳务输出':
        raise Error(no='5_17_013', outInfo=record.outInfo,objectInfo=[record.objectInfo])
