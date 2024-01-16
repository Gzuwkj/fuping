from model import Person
from error import Error
from typing import Dict, List
# id2record: Dict[str, List[Person]] = {}
from datetime import datetime

def process(record: Person):
    if record.objectInfo is None:
        return
    if (record.idCard is None) or (len(record.idCard) not in [18, 20, 22]):
        return
    elif len(record.idCard) == 18:
        a = record.idCard[6:-4]
    elif len(record.idCard) == 20:
        a = record.idCard[6:-6]
    elif len(record.idCard) == 22:
        a = record.idCard[6:-8]
    a = list(a)
    a.insert(4, '-')
    a.insert(7, '-')
    str_i = ''.join(a)
    age = age_calc(str_i)
    # 5_17_004-脱贫人口高中和中职教育小于15岁和大于20岁
    if record.objectInfo['户类型'] == '脱贫户' and (record.objectInfo['在校生状况'] in ["普通高中一年级","普通高中二年级","普通高中三年级","中职一年级",\
        "中职二年级","中职三年级"]) \
        and (age < 15 or age > 20 ):
        raise Error(no='5_17_004', objectInfo=[record.objectInfo])



def age_calc(birth_date):
    end_date=datetime.now().strftime('%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    # change the type of date to datetime
    birth_date = datetime.strptime(birth_date, '%Y-%m-%d')

    # compute the difference of day, month and year
    day_diff = end_date.day - birth_date.day
    month_diff = end_date.month - birth_date.month
    year_diff = end_date.year - birth_date.year

    # compute age based on the diffference of day, month and year
    if day_diff >= 0:
        if month_diff >= 0:
            years_old = year_diff
        else:
            years_old = year_diff - 1
    else:
        if month_diff >= 1:
            years_old = year_diff
        else:
            years_old = year_diff - 1
    return years_old