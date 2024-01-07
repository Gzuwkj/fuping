from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}


# 监测对象家庭成员中有未参加城乡居民（职工）基本医疗保险但未享受健康帮扶和社会帮扶其中一项
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['是否有家庭成员未参加城乡居民（职工）基本医疗保险'] == '否' or record.objectInfo['是否有家庭成员未参加城乡居民（职工）基本医疗保险'] == '':
        if record.objectInfo['健康帮扶'] == '' and record.objectInfo['社会帮扶'] == '':
            raise Error(no=os.path.basename(__file__), objectInfo=[record.objectInfo],
                        msg='监测对象家庭成员中有未参加城乡居民（职工）基本医疗保险但未享受健康帮扶和社会帮扶其中一项')
