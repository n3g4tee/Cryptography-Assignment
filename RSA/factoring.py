from factordb.factordb import FactorDB
N = 510143758735509025530880200653196460532653147
db = FactorDB(N)
db.connect()
print(db.get_factor_list())