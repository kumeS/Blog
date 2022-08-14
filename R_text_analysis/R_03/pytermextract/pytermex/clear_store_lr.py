#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
usage:
  python clear_store_lr.py

"""

import dbm

if __name__ == "__main__":
    DB = dbm.open("store-lr", "n")
    DB.close()
