# -*- coding: utf-8 -*-
"""my_report_helpers.py -- Vitesse Python shared extraction utilities (template 5).
Deploy to: Vitesse\Lib\my_report_helpers.py
Compatible with Python 2.6 ONLY.
"""
import kcs_dex, kcs_util

ok = kcs_util.success()

def get_integer(est):
    res = kcs_dex.extract(est)
    if res == ok:
        typ = kcs_dex.next_result()
        if typ == 1:
            return kcs_dex.get_int()
    return None

def get_real(est):
    res = kcs_dex.extract(est)
    if res == ok:
        typ = kcs_dex.next_result()
        if typ == 2:
            return kcs_dex.get_real()
    return None

def get_string(est):
    res = kcs_dex.extract(est)
    if res == ok:
        typ = kcs_dex.next_result()
        if typ == 3:
            return kcs_dex.get_string()
    return None

def get_rea_list(est):
    res = kcs_dex.extract(est)
    if res == ok:
        typ = kcs_dex.next_result()
        if typ > 10:
            n = typ - 10
            return [kcs_dex.get_indexedreal(i) for i in range(n)]
    return []
