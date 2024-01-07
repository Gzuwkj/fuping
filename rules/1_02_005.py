from model import Person
from error import Error
from typing import Dict, List


'''
规则：脱贫户有义务教育阶段适龄儿童不在校但未纳入易返贫致贫户
思路：每个脱贫户判断户主的家庭成员是否有义务教育阶段适龄儿童不在校但未纳入易返贫致贫户；
     易返贫致贫户的判断准则根据（自定义）监测对象表格的检测对象类别一列为要求，其中信息为
     ['脱贫不稳定户', '边缘易致贫户']的为易返贫致贫户。
完成！！！
'''
id2record:Dict[str, List[Person]] = {}
unstable_types = ['脱贫不稳定户', '边缘易致贫户']
def process(record: Person):
    if record.objectInfo is None:
        return
    dropout_children = []
    error_list = []
    if record.objectInfo.get('户类型') == '脱贫户' and record.family.host.idCard not in id2record:
        for member in record.family.member:
            if member.objectInfo.get('是否义务教育阶段适龄儿童少年失学辍学') == '是':
                dropout_children.append(member.objectInfo)
    id2record[record.family.host.idCard] = record.family.host
    if len(dropout_children) != 0:
        for member in record.family.member:
            if member.objectInfo.get('检测对象类别') not in unstable_types:
                error_list.append(member.objectInfo)
        msg = '脱贫户{}有{}名义务教育阶段适龄儿童不在校但未纳入易返贫致贫户'.format(record.objectInfo.get('户编号'), len(dropout_children))
        raise Error(no='1_02_005', objectInfo=error_list, msg=msg)
