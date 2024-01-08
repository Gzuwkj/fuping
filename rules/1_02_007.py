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
    if record.objectInfo.get('户类型') == '脱贫户' and record.family.host.idCard not in id2record:
        error_list = []
        for member in record.family.member:
            if member.objectInfo.get('是否解决安全饮用水') == '否' or member.objectInfo.get('是否危房户') == '是':
                error_list.append(member.objectInfo)

        for member in record.family.member:
            if str(member.objectInfo.get('是否参加城乡居民基本医疗保险')) == '否' and str(member.objectInfo.get('是否参加城镇职工基本医疗保险')) == '否':
                error_list.append(member.objectInfo)

        for member in record.family.member:
            if member.objectInfo.get('是否义务教育阶段适龄儿童少年失学辍学') == '是' and len(str(member.objectInfo.get('义务教育阶段未上学原因'))) == 0:
                error_list.append(member.objectInfo)
        if len(error_list) != 0:
            raise Error(no='1_02_007.py', record=error_list)

    id2record[record.family.host.idCard] = record.family.host

