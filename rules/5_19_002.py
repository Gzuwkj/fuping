from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}


# 脱贫户“是否饮水安全”为空值
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['户类型'] == '脱贫户':
        if record.objectInfo['是否解决安全饮用水'] == '':
            raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                        msg='脱贫户“是否饮水安全”为空值')
