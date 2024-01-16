from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None or record.objectInfo['识别监测时间']=='':
        return
        # 1111_06-2 023年3月及以前识别的未消除风险监测对象未登记城乡居民基本医疗保险个人缴费补贴措施
    time = 0
    if 202303>=int(float(record.objectInfo['识别监测时间'])) >= 202210:
        time = 1
    if ('城乡居民基本医疗保险个人缴费补贴' not in record.objectInfo['健康帮扶']) and time and record.objectInfo['风险是否已消除'] == '否' and \
                record.objectInfo['监测对象类别'] != '':
        raise Error(no='1111_06', objectInfo=[record.objectInfo])

    # 用基础信息表中DE列“风险是否已消除”、DF列“识别监测时间”结合ET列“健康帮扶”判断。
    # 如DE列“风险是否已消除”数据值为“否”，DF列“识别监测时间”数据值为“202210 - 202303”
    # 但ET列“健康帮扶”数据值不为“参加城乡居民基本医疗保险个人缴费补贴”则为问题。（
    # 该问题规则要以每年医保部门补贴截止时间为准，如2024年补贴截止时间2024年2月，
    # 识别时间为2024年2月以后监测户不享受此政策，以此更新问题规则时间数据）