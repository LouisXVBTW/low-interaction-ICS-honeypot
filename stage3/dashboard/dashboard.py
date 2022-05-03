from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

import os, sys, json
filename = os.path.dirname(__file__)
sys.path.append(filename+"/../database")
from fetchfromDB import read_protocols, read_ips, read_geo
app = FastAPI()

templates = Jinja2Templates(directory="templates")



@app.get("/", response_class=FileResponse)
async def readIndex(request: Request):
    allbars = []
    protocolsPie = read_protocols()
    ipsPie = read_ips()
    countryANDcity = read_geo()
    print (countryANDcity)
    
    # Need to add an "Other" to represend the rest that was less than the top 10. for all of these. 

    allbars.append(["ipsBar", "IP Interaction Count", list(map(lambda x:x['ip'], ipsPie)), list(map(lambda x:x["ipCount"], ipsPie))])
    allbars.append(["protocolsBar", "Protocol Interaction Count", list(map(lambda x:x["protocol"], protocolsPie)), list(map(lambda x: x["protocolCount"], protocolsPie))])
    allbars.append(["country", "Country Interaction Count", countryANDcity[0], countryANDcity[1]])
    allbars.append(["city", "City Interaction Count", countryANDcity[2], countryANDcity[3]])
    context = {"request": request, "testItems": protocolsPie, "allbars": allbars}
    return templates.TemplateResponse("index.html", context)

@app.get("/htmx.js")
def getHTMX(request: Request):
    path = filename+"/scripts/htmx.js"
    return FileResponse(path)

@app.get("/tailwindcss.js")
def getHTMX(request: Request):
    path = filename+"/scripts/tailwindcss.js"
    return FileResponse(path)
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
