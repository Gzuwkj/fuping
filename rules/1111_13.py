from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None or record.objectInfo['识别监测时间']=='':
        return
        # 1111_13- 4月份及后识别监测对象登记参加城乡居民基本医疗保险个人缴费补贴
    time = 0

    if int(float(record.objectInfo['识别监测时间'])) >= 202304:
        time = 1
    if record.objectInfo['风险是否已消除'] == '否' and record.objectInfo['监测对象类别'] != '' and \
            ( '城乡居民基本医疗保险个人缴费补贴'  in record.objectInfo['健康帮扶']) and time:
        raise Error(no='1111_13', objectInfo=[record.objectInfo])

    # 用M列“监测对象类别”结合DF列“识别监测时间”结合ET列“健康帮扶”判断。
    # 如DE列“风险是否已消除”数据值为“否”，DF列“识别监测时间”数据值大于“202304”
    # 但ET列“健康帮扶”数据值为“参加城乡居民基本医疗保险个人缴费补贴”则为问题。
    # （该问题规则要以每年医保部门补贴截止时间为准，如2024年补贴截止时间2024年2月，以此更新问题规则时间数据）