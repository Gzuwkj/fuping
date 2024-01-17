from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}


# 监测户“是否危房”为空值
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['监测对象类别'] != '':
        if record.objectInfo['是否危房户'] == '' or record.objectInfo['是否危房户'] == '是':
            raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                        msg='监测户“是否危房”为空值')

