from model import Person
from error import Error

def process(record: Person):

    # 3_02_003 - 脱贫户“有无卫生厕所”为空
    if record.huInfo  is None:
        return
    if record.huInfo['户类型'] == '脱贫户' and record.huInfo['卫生厕所是否能正常使用']=='' :
        raise Error(no='3_02_003', huInfo=record.huInfo)