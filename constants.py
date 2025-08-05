# -*- encoding: utf-8 -*-
"""
@File    : constants.py
@Author  : Wenhao Qi
@Version : 1.0
@Contact : wenhaoqi51@gmail.com
@License : (C)Copyright 2023-2026, CASIA
"""

# 模型说明
MODEL_EXPLAIN = {
    "10001": "夺取制权行动模型"
}
MODELS = [10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009, 10010, 10011, 10012, 10013, 10014]


class ModelsStrToInt:
    AccessControl = 10001
    EnemySharingSystem = 10002


# 常见的HTTP返回码
class ResponseStatus:
    SUCCESS = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500


class ResponseMessage:
    SUCCESSFUL_OPERATION = "Operation completed successfully."
    MISSING_PARAMETERS = "Missing parameters."
    INVALID_PARAMETERS = "Invalid parameters."
    INTERNAL_SERVER_ERROR = "Internal server error."


# 标准响应结构生成函数
def make_response(res_code=ResponseStatus.SUCCESS, res_msg=ResponseMessage.SUCCESSFUL_OPERATION, data=None):
    if data is None:
        data = {}
    return {
        "res_code": res_code,
        "res_msg": res_msg,
        "data": data
    }
