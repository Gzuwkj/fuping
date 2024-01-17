# -*- coding: utf-8 -*-
from datetime import datetime

from model import Person
from error import Error
from typing import Dict, List

id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.objectInfo is None or record.family is None:
        return

    for member in record.family.member:
        if member.objectInfo:
            relation = member.objectInfo.get("与户主关系")
            gender = member.objectInfo.get("性别")
            head_gender = member.family.host.objectInfo.get("与户主关系")
            if relation == "配偶":
                # 配偶性别与户主性别不能相同
                if head_gender == gender:
                    raise Error(no='2_12_008', objectInfo=[record.objectInfo, member.objectInfo],
                                msg="监测对象家庭成员与户主关系与性别指标值逻辑关系错误")
            elif relation in ["女儿", "母亲", "兄弟媳妇", "祖母", "孙女"]:
                # 之女 之母 兄弟媳妇 之祖母 之孙女必须为2
                if gender != "2":
                    raise Error(no='2_12_008', objectInfo=[record.objectInfo, member.objectInfo],
                                msg="监测对象家庭成员与户主关系与性别指标值逻辑关系错误")
            elif relation in ["父亲", "儿子", "女婿", "孙子"]:
                # 之父，之子，之女婿 之孙子必须为1
                if gender != "1":
                    raise Error(no='2_12_008', objectInfo=[record.objectInfo, member.objectInfo],
                                msg="监测对象家庭成员与户主关系与性别指标值逻辑关系错误")


