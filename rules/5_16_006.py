from model import Person
from error import Error

'''5_16_006-未消除风险防止返贫监测对象家中无人享受特困供养但帮扶措施登记特困供养名单（含自然减少人员）'''


def process(record: Person):
    if record.objectInfo is None:
        return
    if (record.objectInfo.get("风险是否已消除") == "否" and int(record.objectInfo.get(
            "特困人员救助供养金")) > 0 and "特困供养" not in record.objectInfo.get("综合保障")):
        raise Error(no='5_16_006', objectInfo=[record.objectInfo])
