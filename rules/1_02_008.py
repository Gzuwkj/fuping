from model import Person
from error import Error
from typing import Dict, List
##1_02_008-已消除返（致）贫风险的防止返贫监测对象户住房出现安全问题
# id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.objectInfo is None:
        return  ##风险是否已消除0
    if record.objectInfo['风险消除后是否住房损毁'] == '是':###record.objectInfo['户类型'] == '脱贫户'  and record.objectInfo['监测对象类别'] != '' and record.objectInfo['风险是否已消除'] == '是' and
        raise Error(no='1_02_008', objectInfo=[record.objectInfo], msg="1_02_009-已消除返（致）贫风险的防止返贫监测对象户zhufnag出现安全问题")
