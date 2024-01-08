from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return
        # 1111_06-2 023年3月及以前识别的未消除风险监测对象未登记城乡居民基本医疗保险个人缴费补贴措施
    time = 0
    if record.objectInfo['识别监测时间'] != '':

        if int(float(record.objectInfo['识别监测时间'])) >= 202303:
            time = 1
    if '城乡居民基本医疗保险个人缴费补贴' not in record.objectInfo['健康帮扶'] and time and record.objectInfo['风险是否已消除'] == '否' and \
                record.objectInfo['监测对象类别'] != '':
        raise Error(no='1111_06', objectInfo=[record.objectInfo])