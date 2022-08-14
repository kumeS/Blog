#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
usage:
  python clear_df.py

"""
import dbm

if __name__ == "__main__":
    DF = dbm.open("df", "n")
    DF.close()
