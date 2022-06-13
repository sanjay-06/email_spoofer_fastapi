from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from spoof import Spoof
from sendmail import Auth

templates=Jinja2Templates(directory="static")

app=FastAPI()

spoof=Spoof()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def getpage(request : Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/login")
def login(request:Request,username:str =Form(...), password:str = Form(...)):
    if(Auth.checkuser(username,password)):
        return templates.TemplateResponse("sendmail.html",{"request":request})
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/sendmail")
def login(request:Request,sendermail:str =Form(...), sendername:str = Form(...),recievermail:str =Form(...), recievername:str = Form(...),subject:str =Form(...), message:str = Form(...)):
    print(sendermail)
    spoof.createmail(sender=sendermail,sendername=sendername,recievername=recievername,reciever=recievermail,subject=subject,body=message)
    spoof.sendmail()   
    spoof.logresponse()
# return templates.TemplateResponse("sendmail.html",{"request":request})
    return templates.TemplateResponse("index.html",{"request":request})

uvicorn.run(app,host='0.0.0.0',port=8000)