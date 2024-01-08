from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}


# 监测对象入户道路是否硬化为空
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['入户道路是否硬化'] == '':
        raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                    msg='监测对象入户道路是否硬化为空')
    
