from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}


# 监测对象风险类型为因残但未享受综合保障和社会帮扶其中一项
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['致贫/返贫风险1'] == '因残' or record.objectInfo['致贫/返贫风险2'] == '因残' or \
            record.objectInfo['致贫/返贫风险3'] == '因残':
        if record.objectInfo['综合保障'] == '' and record.objectInfo['社会帮扶'] == '':
            raise Error(no=os.path.basename(__file__), objectInfo=[record.objectInfo],
                        msg='监测对象风险类型为因残但未享受综合保障和社会帮扶其中一项')
