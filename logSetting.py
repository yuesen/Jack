# -*- coding: utf-8 -*-

"""
日志文件
"""

import os
import logging
import logging.handlers


def init_log(log_path, level=logging.INFO, when="D", backup=7):
    formatter = logging.Formatter(
        "%(levelname)s: %(asctime)s: %(filename)s:%(lineno)d * %(thread)d %(message)s",
        "%m-%d %H:%M:%S")
    logger = logging.getLogger()
    logger.setLevel(level)

    dir_path = os.path.dirname(log_path)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

    # 记录常规info
    info = logging.handlers.TimedRotatingFileHandler(log_path + ".log", when=when, backupCount=backup)
    info.setLevel(level)
    info.setFormatter(formatter)
    logger.addHandler(info)

    # 记录warning
    err = logging.handlers.TimedRotatingFileHandler(log_path + ".log.wf", when=when, backupCount=backup)
    err.setLevel(logging.WARNING)
    err.setFormatter(formatter)
    logger.addHandler(err)

    # 输出到控制台
    console = logging.StreamHandler()
    console.setLevel(level)
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger
