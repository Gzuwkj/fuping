from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}


# 5_18_006-监测对象风险类型为因安全饮水但未登记饮水安全保障措施
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['监测对象类别'] != '':
        if record.objectInfo['致贫/返贫风险1'] == '因安全饮水' or \
                record.objectInfo['致贫/返贫风险2'] == '因安全饮水' or \
                record.objectInfo['致贫/返贫风险3'] == '因安全饮水' or \
                record.objectInfo['致贫/返贫风险4'] == '因安全饮水' or \
                record.objectInfo['致贫/返贫风险5'] == '因安全饮水':
            if record.objectInfo['饮水安全保障'] == '':
                raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                            msg='5_18_006-监测对象风险类型为因安全饮水但未登记饮水安全保障措施')
