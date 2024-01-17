'''
5_12_007-未消除防止防贫监测对象且家中有劳动力（含弱半）户未落实开发式帮扶（劳动力：普通劳动力、技能劳动力；开发式帮扶：产业帮扶、就业帮扶、金融帮扶、公益性岗位）
5_12_007-全省有劳动力且未消除风险的防止返贫监测对象未落实开发式帮扶措施(识别6个月及以上)
'''
from model import Person
from error import Error
from datetime import datetime





def process(record: Person):
    process200(record)
    process231(record)


def process231(record: Person):
    if record.objectInfo is None:
        return


def process200(record: Person):
    if record.objectInfo is None:
        return
    if (
            record.objectInfo.get("劳动技能") in ["普通劳动力", "弱劳动力或半劳动力", "技能劳动力"]
            and record.objectInfo.get("风险是否已消除") == "否"
            and all(
        record.objectInfo.get(key) == "" for key in ["产业帮扶", "公益岗位帮扶", "就业帮扶", "金融帮扶"]
    )
            and (
            record.objectInfo.get("实施开发式帮扶措施情况") == ""
            or record.objectInfo.get("实施开发式帮扶措施情况") == "尚未实施"
    )
    ):
        raise Error(no='5_12_007_200', objectInfo=[record.objectInfo])
