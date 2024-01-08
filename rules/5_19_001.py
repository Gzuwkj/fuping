from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}


# 脱贫人口是否参加城乡居民（城镇职工）基本养老保险同时为空值
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['户类型'] == '脱贫户':
        if record.objectInfo['是否参加城镇职工基本养老保险'] == '' or record.objectInfo['是否参加城乡居民基本养老保险'] == '':
            raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                        msg='脱贫人口是否参加城乡居民（城镇职工）基本养老保险同时为空值')
