# -*- encoding: utf-8 -*-
"""
@File    : config.py
@Author  : Wenhao Qi
@Version : 1.0
@Contact : wenhaoqi51@gmail.com
@License : (C)Copyright 2023-2026, CASIA
"""
import os

# 工程目录
DIR_PATH = os.path.dirname(__file__)

# 默认区域的经纬度坐标，4个顶点, 按照最小经度->最小纬度->最大经度->最大纬度的顺序排列
DEFAULT_COORD = [
    117, 21,
    123, 27
]

# 网格划分的大小，10进制偏移量
GRID_SIZE = 0.3


# --------------------------配置达梦数据库连接--------------------------------
class DmConfig:
    USERNAME = "SYSDBA"
    PASSWORD = "SYSDBA"
    IP = os.getenv("DM_DB_IP", "192.168.22.201")
    PORT = os.getenv("DM_DB_PORT", "5236")
    USER_GROUP = "zlzyyx"
    CHARSET = "UTF8"
    DATABASE = ''


# 配置数据库URI
SQLALCHEMY_DATABASE_URI = r'dm+dmPython://{}:{}@{}:{}/{}'.format(
    DmConfig.USERNAME,
    DmConfig.PASSWORD,
    DmConfig.IP,
    DmConfig.PORT,
    DmConfig.DATABASE
)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# -----------------------配置Celery数据库-----------------
CELERY_REDIS_BROKER = 'redis://localhost:6379/0'

# ----服务地址-----
HOST = "0.0.0.0"
PORT = 5500
DEBUG = True
