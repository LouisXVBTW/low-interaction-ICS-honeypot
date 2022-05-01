from fetchfromDB import read_DB


protocolsPie = read_DB()
pnames = list(map(lambda x:str(x["protocol"]), protocolsPie))

print (type(pnames))