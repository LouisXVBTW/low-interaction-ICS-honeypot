from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

import os, sys, json
filename = os.path.dirname(__file__)
sys.path.append(filename+"/../database")
from fetchfromDB import read_protocols, read_ips, read_geo

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/chart.min.js")
def getHTMX(request: Request):
    path = filename+"/scripts/chart.min.js"
    return FileResponse(path)
@app.get("/makeCharts.js")
def getHTMX(request: Request):
    path = filename+"/scripts/makeCharts.js"
    return FileResponse(path)
@app.get("/style.css")
def getHTMX(request: Request):
    path = filename+"/css/styles.css"
    return FileResponse(path)

@app.get("/", response_class=FileResponse)
async def readIndex(request: Request):
    allbars = []
    protocolsPie = read_protocols()
    ipsPie = read_ips()
    countryANDcity = read_geo()    
    
    allbars.append(["ipsBar", "IP Interaction Count", list(map(lambda x:x['ip'], ipsPie)), list(map(lambda x:x["ipCount"], ipsPie))])
    allbars.append(["protocolsBar", "Protocol Interaction Count", list(map(lambda x:x["protocol"], protocolsPie)), list(map(lambda x: x["protocolCount"], protocolsPie))])
    allbars.append(["country", "Country Interaction Count", countryANDcity[0], countryANDcity[1]])
    allbars.append(["city", "City Interaction Count", countryANDcity[2], countryANDcity[3]])
    context = {"request": request, "testItems": protocolsPie, "allbars": allbars}
    return templates.TemplateResponse("index.html", context)



