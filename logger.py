# -*- coding: utf-8 -*-
"""
@File  :logger.py
@Author:Sapphire
@Date  :2021/5/5 2:45
@Desc  :
"""
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='fastapi.log'
)
logger = logging.getLogger(__name__)
