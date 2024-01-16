from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["风险是否已消除"] == "是":
        if (
            record.objectInfo["致贫/返贫风险1"] == "因学"
            or record.objectInfo["致贫/返贫风险2"] == "因学"
            or record.objectInfo["致贫/返贫风险3"] == "因学"
            or record.objectInfo["致贫/返贫风险4"] == "因学"
            or record.objectInfo["致贫/返贫风险5"] == "因学"
        ):
            if (
                record.objectInfo["教育帮扶"] == ""
                and record.objectInfo["义务教育保障"] == ""
                and record.objectInfo["社会帮扶"] == ""
            ):
                raise Error(no="3_11_004", objectInfo=[record.objectInfo])


# def process(record: Person):
#     if record.objectInfo is None:
#         return
#     if record.objectInfo["风险消除方式"] == "帮扶消除":
#         if (record.objectInfo["致贫/返贫风险1"] == "因学" or record.objectInfo["致贫/返贫风险2"] == "因学" or
#                 record.objectInfo["致贫/返贫风险3"] == "因学" or record.objectInfo["致贫/返贫风险4"] == "因学" or
#                 record.objectInfo["致贫/返贫风险5"] == "因学"):
#             res = False
#             if record.objectInfo["教育帮扶"] != "":
#                 res = True
#             if record.objectInfo["义务教育保障"] != "":
#                 res = True
#             if record.objectInfo["社会帮扶"] != "":
#                 res = True
#             if res == False:
#                 raise Error(no='3_11_004', objectInfo=[record.objectInfo])
