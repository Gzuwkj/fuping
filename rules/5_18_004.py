from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}


# 监测对象风险类型为因安全住房但未登记住房安全保障和搬迁其中一项
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['监测对象类别'] != '':
        if record.objectInfo['致贫/返贫风险1'] == '因安全住房' or \
                record.objectInfo['致贫/返贫风险2'] == '因安全住房' or \
                record.objectInfo['致贫/返贫风险3'] == '因安全住房' or \
                record.objectInfo['致贫/返贫风险4'] == '因安全住房' or \
                record.objectInfo['致贫/返贫风险5'] == '因安全住房':
            if record.objectInfo['住房安全保障'] == '' or record.objectInfo['搬迁'] == '':
                raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                            msg='监测对象风险类型为因安全住房但未登记住房安全保障和搬迁其中一项')
