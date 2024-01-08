from model import Person
from error import Error
from typing import Dict, List


'''
规则：监测对象户（致）贫风险为空
思路：（自定义）监测对象信息表中有致贫/返贫风险1，致贫/返贫风险2，致贫/返贫风险3，致贫/返贫风险4，致贫/返贫风险5，
     5个列表示风险信息，监测对象户范围为表格中的全部户，以户编号相同的为一组，家庭成员中全部致贫/返贫风险1都为空的话判定为监测对象户（致）贫风险为空
完成！！！
'''
huID = []
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo.get('户编号') not in huID:
        result = True
        error_list = []
        for member in record.family.member:
            if len(str(member.objectInfo.get('致贫/返贫风险1')).strip()) != 0:
                result = False
            else:
                error_list.append(member.objectInfo)

        if result:
            msg = '监测对象户{}（致）贫风险为空'.format(record.objectInfo.get('户编号'))
            raise Error(no='1_11_001', objectInfo=error_list, msg=msg)
    huID.append(record.objectInfo.get('户编号'))


