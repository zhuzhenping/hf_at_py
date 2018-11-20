#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = '项目配置信息'
__author__ = 'HaiFeng'
__mtime__ = '20180820'

import yaml
import os
# from sqlalchemy import create_engine
# from sqlalchemy.engine import Engine
import shutil
from color_log.logger import Logger


class Config(object):
    """"""

    def __init__(self):
        self.log = Logger()
        origin_cfg_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.yml')
        cfg_file = os.path.join(os.getcwd(), 'config.yml')
        if not os.path.exists(cfg_file):
            shutil.copy(origin_cfg_file, cfg_file)
        cfg = yaml.load(open(cfg_file, 'r', encoding='utf-8'))

        # 追单设置
        self.chasing = cfg['ctp_config']['chasing']

        self.stra_path = cfg['stra_path']
        self.cfg_zmq = ''
        if 'zmq_config' in cfg:
            self.cfg_zmq = cfg['zmq_config']
        self.engine_postgres = None
        # if 'postgres_config' in cfg:
        #     self.engine_postgres = create_engine(cfg['postgres_config'])

        self.front_trade = ''
        self.front_quote = ''
        self.broker = ''
        self.investor = ''
        self.pwd = ''
        cfg_ctp = cfg['ctp_config']
        if cfg_ctp['ctp_front'] != '':
            self.front_name = cfg_ctp['ctp_front']
            cfg_ctp_front = cfg_ctp['fronts'][self.front_name]
            self.front_trade = cfg_ctp_front['trade']
            self.front_quote = cfg_ctp_front['quote']
            self.broker = cfg_ctp_front['broker']
            if 'investor' in cfg_ctp and cfg_ctp['investor'] != '':
                self.investor = cfg_ctp['investor']
            if 'password' in cfg_ctp and cfg_ctp['password'] != '':
                self.pwd = cfg_ctp['password']

        self.single_order_one_bar = False
        '''是否每根K线只发一次指令'''

        self.real_order_enable = False
        '''是否实际对接口发单'''

        self.running_as_server = False
        '''是否作为服务7*24运行'''

        if 'onoff' in cfg:
            cfg_of = cfg['onoff']
            if 'running_as_server' in cfg_of:
                self.running_as_server = cfg_of['running_as_server']
            if 'single_order_one_bar' in cfg_of:
                self.single_order_one_bar = cfg_of['single_order_one_bar']
            if 'real_order_enable' in cfg_of:
                self.real_order_enable = cfg_of['real_order_enable']
