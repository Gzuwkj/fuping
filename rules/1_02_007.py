from model import Person
from error import Error
from typing import Dict, List


'''
规则1：脱贫户未解决两不愁三保障（含监测对象医疗未保障）
规则2：脱贫户未解决两不愁三保障（含监测对象住房饮水未保障）
规则1：脱贫户未解决两不愁三保障（含监测对象教育未保障）
思路：每个脱贫户家庭根据户主只判断一次,分三个规则分别判断并返回错误列表
完成！！！
'''
id2record:Dict[str, List[Person]] = {}
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo.get('户编号') == '10002109164':
        print()
    if record.objectInfo.get('户类型') == '脱贫户' and record.family.host.idCard not in id2record:
        error_list_1 = []
        for member in record.family.member:
            if member.objectInfo.get('是否解决安全饮用水') == '否' or member.objectInfo.get('是否危房户') == '是':
                error_list_1.append(member.objectInfo)
        if len(error_list_1) != 0:
            try:
                msg_1 = '脱贫户{}有{}名家庭成员住房饮水未保障'.format(record.objectInfo.get('户编号'), len(error_list_1))
                raise Error(no='1_02_007.py', objectInfo=error_list_1, msg=msg_1)
            except Error as e:
                    pass
        error_list_2 = []
        for member in record.family.member:
            if str(member.objectInfo.get('是否参加城乡居民基本医疗保险')) == '否' and str(member.objectInfo.get('是否参加城镇职工基本医疗保险')) == '否':
                error_list_2.append(member.objectInfo)
        if len(error_list_2) != 0:
            try:
                msg_2 = '脱贫户{}有{}名家庭成员医疗未保障'.format(record.objectInfo.get('户编号'), len(error_list_2))
                raise Error(no='1_02_007.py', objectInfo=error_list_2, msg=msg_2)
            except Error as e:
                pass
        error_list_3 = []
        for member in record.family.member:
            if member.objectInfo.get('是否义务教育阶段适龄儿童少年失学辍学') == '是' and len(str(member.objectInfo.get('义务教育阶段未上学原因'))) == 0:
                error_list_3.append(member.objectInfo)
        if len(error_list_3) != 0:
            try:
                msg_3 = '脱贫户{}有{}名家庭成员教育未保障'.format(record.objectInfo.get('户编号'), len(error_list_3))
                raise Error(no='1_02_007.py', record=error_list_3, msg=msg_3)
            except Error as e:
                pass
    id2record[record.family.host.idCard] = record.family.host

