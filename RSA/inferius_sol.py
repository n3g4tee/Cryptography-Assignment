from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes
from factordb.factordb import FactorDB
N = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373
#db = FactorDB(N)
#db.connect()
#print(db.get_factor_list())
p,q=752708788837165590355094155871, 986369682585281993933185289261
phi = (p-1)*(q-1)
#e*d = 1 mod phi(N) <=> d= e^-1 mod phi(N)
d=inverse(e,phi)
# flag^e % N // ct^d % N
pt=pow(ct,d,N)
flag=long_to_bytes(pt)
print(flag)
