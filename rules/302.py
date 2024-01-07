from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}


# 监测对象文化程度为大专及以上但未务工就业
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['文化程度'] == '大专' or record.objectInfo['文化程度'] == '本科及以上':
        if record.outInfo is None:
            raise Error(no=os.path.basename(__file__), objectInfo=[record.objectInfo],outInfo=record.outInfo,
                        msg='监测对象文化程度为大专及以上但未务工就业')

