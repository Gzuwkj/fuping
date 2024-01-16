from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime

'''
规则：脱贫人口失学或辍学原因为因病或因残但健康状况为健康
完成！！！！
'''


def process(record: Person):
    if record.objectInfo is None:
        return

    if str(record.objectInfo.get('户类型')) == '脱贫户':
        if  record.objectInfo.get('义务教育阶段未上学原因') == '因病' or record.objectInfo.get('义务教育阶段未上学原因') == '因残':
            if record.objectInfo.get('健康状况') == '健康':
                raise Error(no='2_01_012', objectInfo=[record.objectInfo])
