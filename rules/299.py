from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}


# 监测户“住房面积”为空值
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['住房面积'] == '':
        raise Error(no=os.path.basename(__file__), objectInfo=[record.objectInfo],
                    msg='监测户“住房面积”为空值')

