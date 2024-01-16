# 出列村各类土地面积小于村内脱贫户该类土地面积之和
from model import DictRecord
from error import Error


# 有问题
def process(record: DictRecord):
    if record is None:
        return

