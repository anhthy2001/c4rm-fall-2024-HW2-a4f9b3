#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:06:19 2025

@author: thynguyen
"""

import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    N = m * ppy  
    couponPayment = (face * couponRate) / ppy  
    period_ytm = y / ppy  
    t = np.arange(1, N + 1)  

    pv_coupons = np.sum(couponPayment / (1 + period_ytm) ** t)

    pv_face_value = face / (1 + period_ytm) ** N

    bond_price = pv_coupons + pv_face_value
    
    return bond_price  

y = 0.03  
face = 2000000  
couponRate = 0.04  
m = 10  


annualBondValue = getBondPrice(y, face, couponRate, m, ppy = 1)

semiBondValue = getBondPrice(y, face, couponRate, m, ppy = 2)
print(f"Bond Price (Annual): ${annualBondValue:.2f}")
print(f"Bond Price (SemiAnnual): ${semiBondValue:.2f}")


