from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

import os, sys, json
filename = os.path.dirname(__file__)
sys.path.append(filename+"/../database")
from fetchfromDB import read_protocols, read_ips
app = FastAPI()

templates = Jinja2Templates(directory="templates")



@app.get("/", response_class=FileResponse)
async def readIndex(request: Request):
    allpies = []
    protocolsPie = read_protocols()
    ipsPie = read_ips()
    allpies.append(["ipsBar", "IP Interaction Count", list(map(lambda x:x['ip'], ipsPie)), list(map(lambda x:x["ipCount"], ipsPie))])
    allpies.append(["protocolsBar", "Protocol Interaction Count", list(map(lambda x:x["protocol"], protocolsPie)), list(map(lambda x: x["protocolCount"], protocolsPie))])
    context = {"request": request, "testItems": protocolsPie, "allpies": allpies}
    return templates.TemplateResponse("index.html", context)

@app.get("/htmx.js")
def getHTMX(request: Request):
    path = filename+"/templates/htmx.js"
    return FileResponse(path)

@app.get("/tailwindcss.js")
def getHTMX(request: Request):
    path = filename+"/templates/tailwindcss.js"
    return FileResponse(path)
@app.get("/chart.min.js")
def getHTMX(request: Request):
    path = filename+"/templates/chart.min.js"
    return FileResponse(path)
@app.get("/makeCharts.js")
def getHTMX(request: Request):
    path = filename+"/templates/makeCharts.js"
    return FileResponse(path)
