from fetchfromDB import read_protocols


protocolsPie = read_protocols()
pnames = list(map(lambda x:str(x["protocol"]), protocolsPie))

print (type(pnames))