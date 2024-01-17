from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}
def process(record: Person):
    if record.objectInfo is None:
        return
    # 5_15_023-未消除风险识别时收入填写不合理（识别时工资性收入大于0小于100）
    if record.objectInfo['监测对象类别'] != '' and record.objectInfo['风险是否已消除'] == '否':
        if record.objectInfo['致贫/返贫风险1'] == '因病' or record.objectInfo['致贫/返贫风险2'] == '因病' or record.objectInfo['致贫/返贫风险3'] == '因病' or record.objectInfo['致贫/返贫风险4'] == '因病' or record.objectInfo['致贫/返贫风险5'] == '因病':
            if record.objectInfo['合规自付支出'] in ['0','']:
                raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                            msg='5_15_020-未消除风险监测对象识别时致贫返贫风险为因病但是识别时合规自付支出为零')





