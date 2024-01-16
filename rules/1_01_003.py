from model import Person
from error import Error
from typing import Dict, List


'''
规则：脱贫户家庭成员身份证号码不符合校验规则（特指18位证件号码）
思路：每个脱贫户判断户主的家庭成员身份证号码是否符合校验规则，避免重复判断；
     校验规则由规定的证件前17位乘以规定的权重取余，证件最后一位对应余数的取值是否一致。
完成！！！
'''
id2record:Dict[str, List[Person]] = {}
checksum_dict = {0:'1', 1:'0', 2:'X', 3:'9', 4:'8', 5:'7', 6:'6', 7:'5', 8:'4', 9:'3', 10:'2'}
def check_id(id: str) -> bool:
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    factors = [int(id[i]) * weights[i] for i in range(17)]
    checksum = sum(factors) % 11
    return checksum_dict.get(checksum) == id[17]

def process(record: Person):
    if record.objectInfo is None:
        return
    error_lists = []
    if record.objectInfo.get('户类型') == '脱贫户' and record.family.host.idCard not in id2record:
        for member in record.family.member:
            if len(member.idCard) == 18:
                if not check_id(member.idCard):
                    error_lists.append(member.objectInfo)
    id2record[record.family.host.idCard] = [record.family.host]
    if len(error_lists) != 0:
        msg = '脱贫户{}有{}名家庭成员证件号码位数异常'.format(record.objectInfo.get('户编号'), len(error_lists))
        raise Error(no='1_01_003', objectInfo=error_lists, msg=msg)
