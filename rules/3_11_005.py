from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["风险是否已消除"] == "是":
        if (
            record.objectInfo["致贫/返贫风险1"] == "因残"
            or record.objectInfo["致贫/返贫风险2"] == "因残"
            or record.objectInfo["致贫/返贫风险3"] == "因残"
            or record.objectInfo["致贫/返贫风险4"] == "因残"
            or record.objectInfo["致贫/返贫风险5"] == "因残"
        ):
            if (
                record.objectInfo["社会帮扶"] == ""
                and record.objectInfo["综合保障"] == ""
            ):
                raise Error(no="3_11_005", objectInfo=[record.objectInfo])
