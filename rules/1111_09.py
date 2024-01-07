from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return
        ##1111_09-未消除风险的防返贫监测对象未享受城乡居民基本医疗保险个人缴费补贴(2023年4月以前识别)
    time = 0
    if record.objectInfo['识别监测时间'] != '':
        if int(float(record.objectInfo['识别监测时间'])) >= 202304:
            time = 1
    if record.objectInfo['风险是否已消除'] == '否' and record.objectInfo['监测对象类别'] != '' and \
                '城乡居民基本医疗保险个人缴费补贴' not in record.objectInfo['健康帮扶'] and time:
        raise Error(no='1111_09', objectInfo=[record.objectInfo])