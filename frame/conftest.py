#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:conftest.py
@time:2020/11/08
"""
import os
import signal

import pytest
import subprocess


@pytest.fixture(scope='module', autouse=True)
def record_vedio():
    command = "scrcpy --record tmp.mp4"
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # print(p)
    yield
    os.kill(p.pid, signal.SIGINT)
