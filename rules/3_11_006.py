from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["风险是否已消除"] == "是":
        if (
            record.objectInfo["致贫/返贫风险1"] == "因安全住房"
            or record.objectInfo["致贫/返贫风险2"] == "因安全住房"
            or record.objectInfo["致贫/返贫风险3"] == "因安全住房"
            or record.objectInfo["致贫/返贫风险4"] == "因安全住房"
            or record.objectInfo["致贫/返贫风险5"] == "因安全住房"
        ):
            if record.objectInfo["住房安全保障"] == "":
                raise Error(no="3_11_006", objectInfo=[record.objectInfo])
