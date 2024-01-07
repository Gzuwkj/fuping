from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}


# 因病有致贫返贫风险的监测对象未登记健康帮扶措施和社会帮扶其中一项
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['致贫/返贫风险1'] == '因病' or record.objectInfo['致贫/返贫风险2'] == '因病' or \
            record.objectInfo['致贫/返贫风险3'] == '因病':
        if record.objectInfo['健康帮扶'] == '':
            raise Error(no=os.path.basename(__file__), objectInfo=[record.objectInfo],
                        msg='因病有致贫返贫风险的监测对象未登记健康帮扶措施和社会帮扶其中一项')
