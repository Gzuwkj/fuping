from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}


# 监测户“是否危房”为空值
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['是否危房户'] == '':
        raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                    msg='监测户“是否危房”为空值')

