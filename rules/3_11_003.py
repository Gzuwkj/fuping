from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["风险是否已消除"] == "是":
        if (
            record.objectInfo["致贫/返贫风险1"] == "因病"
            or record.objectInfo["致贫/返贫风险2"] == "因病"
            or record.objectInfo["致贫/返贫风险3"] == "因病"
            or record.objectInfo["致贫/返贫风险4"] == "因病"
            or record.objectInfo["致贫/返贫风险5"] == "因病"
        ):
            if (
                record.objectInfo["健康帮扶"] == ""
                and record.objectInfo["社会帮扶"] == ""
                and record.objectInfo["综合保障"] == ""
            ):
                raise Error(no="3_11_003", objectInfo=[record.objectInfo])


# def process(record: Person):
#     if record.objectInfo is None:
#         return
#     if record.objectInfo["风险消除方式"] == "帮扶消除":
#         if (record.objectInfo["致贫/返贫风险1"] == "因病" or record.objectInfo["致贫/返贫风险2"] == "因病" or
#                 record.objectInfo["致贫/返贫风险3"] == "因病" or record.objectInfo["致贫/返贫风险4"] == "因病" or
#                 record.objectInfo["致贫/返贫风险5"] == "因病"):
#             res = False
#             if record.objectInfo["健康帮扶"] != "":
#                 res = True
#             if record.objectInfo["社会帮扶"] != "":
#                 res = True
#             if record.objectInfo["综合保障"] != "":
#                 res = True
#             if res == False:
#                 raise Error(no='3_11_003', objectInfo=[record.objectInfo])
