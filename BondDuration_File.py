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

def getBondDuration(y, face, couponRate, m, ppy=1):
    
    bondValue = getBondPrice(y, face, couponRate, m, ppy)
    couponPayment = (couponRate * face) / ppy
    periods = m * ppy
    period_ytm = y / ppy
    t = np.arange(1, periods + 1)

    weightedPV = np.sum((t / ppy) * (couponPayment / ((1 + period_ytm) ** t))) 
    weightedPV += (periods / ppy) * (face / ((1 + period_ytm) ** periods)) 

    bondDuration = weightedPV / bondValue
    return round(bondDuration, 2)  


y = 0.03  
couponRate = 0.04  
face = 2000000  
m = 10  

Duration_annual = getBondDuration(y, face, couponRate, m, ppy=1)  
Duration_semiannual = getBondDuration(y, face, couponRate, m, ppy=2)  

print(f"Annual Bond Duration: {Duration_annual}") 
print(f"Semiannual Bond Duration: {Duration_semiannual}")  
