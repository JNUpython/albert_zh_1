#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from configparser import ConfigParser


class Config:

    def __init__(self):
        config_path = os.path.split(os.path.realpath(__file__))[0]
        config_path = os.path.join(config_path, "config.ini")
        config = ConfigParser()
        config.read(config_path, encoding="utf-8")
        self.config = config

    def get_model_tiny_bert(self, key):
        return self.config.get("model_tiny_bert", key)

    def get_ipe_punishment_classify(self, key):
        return self.config.get("ipe_punishment_classify", key)

    def get_lcqmc_classify(self, key):
        return self.config.get("lcqmc_classify", key)


config = Config()
