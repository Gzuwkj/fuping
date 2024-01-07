from model import Person
from error import Error
import re

def check_phone(number):
    pattern = r'^1[3456789]\d{9}$'  # 手机号码格式为1开头，第二位数字为3、4、5、6、7、8或者9，后面跟着9位数字

    if re.match(pattern, number):
        return True
    else:
        return False

def process(record: Person):
    if record.objectInfo is None:
        return


    phoneStr = str(record.objectInfo.get('家庭成员联系电话')).split('.')[0]
    if record.objectInfo.get('户类型') == '脱贫户' \
        and len(record.objectInfo.get('监测对象类别')) != 0 \
        and not check_phone(phoneStr):
        raise Error(no='5_13_003', objectInfo=record.objectInfo
                    , msg='监测对象户联系电话为空或不符合规则')


