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


def getBondDuration(y, face, couponRate, m, ppy):
    bondValue = getBondPrice(y, face, couponRate, m, ppy)
    couponPayment = (couponRate * face) / ppy
    periods = m * ppy
    period_ytm = y / ppy
    t = np.arange(1, periods + 1)


    weightedPV = np.sum((t * couponPayment) / ((1 + period_ytm) ** t))
    weightedPV_face_value = (periods * face) / ((1 + period_ytm) ** periods)
    weightedPV = weightedPV + weightedPV_face_value

    bondDuration = weightedPV / bondValue
    return bondDuration

y = 0.03
couponRate = 0.04
face = 2000000
m = 10
ppy = 1


Duration = getBondDuration(y, face, couponRate, m, ppy)


print(f"Bond Duration: {Duration:.2f}")
