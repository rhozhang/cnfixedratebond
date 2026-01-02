from cnfixedratebond import FixedRateBond as FRB
from datetime import date

# basic info: 25国债22
maturity = date(2035, 11, 15)
coupon = 0.0178
freq = 2

# instantiation
b = FRB(maturity, coupon, freq)

# basic info: trading
settle = date(2025, 12, 31)
mkt = 'szse'
prc = 99.947

# attributes
b.couponrate
b.maturitydate
b.frequency

# years residual
b.yearsresidual(settle)

# number of coupon payments
b.coupnum(settle)

# previous coupon payment date
b.couppcd(settle)

# next coupon payment date
b.coupncd(settle)

# accrued interests
b.accrint(settle)

# theoretical clean price (yld = 0.03)
yld = 0.03
b.price(settle, yld, dcc = 'szse')

# yield to maturity (price = prc)
y = b.ytm(settle, prc, dcc = 'szse')

# duration (yld = y)
b.duration(settle, y)

# convexity (yld = y)
b.convexity(settle, y)
