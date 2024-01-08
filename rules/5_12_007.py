'''5_12_007-全省有劳动力且未消除风险的防止返贫监测对象未落实开发式帮扶措施(识别6个月及以上)'''
from model import Person
from error import Error
from datetime import datetime

def calculate_age(id_card):
    # 假设身份证号码格式为18位
    birth_date_str = id_card[6:14]  # 截取身份证号码中的出生日期部分
    birth_date = datetime.strptime(birth_date_str, "%Y%m%d")

    # 获取当前日期
    current_date = datetime.now()

    # 计算年龄
    age = current_date.year - birth_date.year - (
                (current_date.month, current_date.day) < (birth_date.month, birth_date.day))

    return age

def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo.get("劳动技能") == "普通劳动力" and record.objectInfo.get("风险是否已消除0") == "否" and record.objectInfo.get("在校生状况") in ["学龄前儿童", "学前教育"]:
        raise Error(no='5_17_001', objectInfo=[record.objectInfo])