from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}


# 监测对象风险类型为因学但未登记义务教育保障、教育帮扶和社会帮扶其中一项
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['致贫/返贫风险1'] == '因学' or record.objectInfo['致贫/返贫风险2'] == '因学' or \
            record.objectInfo['致贫/返贫风险3'] == '因学':
        if record.objectInfo['义务教育保障'] == '' and record.objectInfo['教育帮扶'] == '' and record.objectInfo['社会帮扶'] == '':
            raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                        msg='监测对象风险类型为因学但未登记义务教育保障、教育帮扶和社会帮扶其中一项')
