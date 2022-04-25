from email.message import Message
from fastapi import FastAPI
import datetime
from slack_sdk.models.blocks.blocks import SectionBlock, Block


app = FastAPI()

def slack_payload():
    now = datetime.datetime.now()
    s1 = str(now.hour)+":"+str(now.minute)
    if datetime.datetime.today().weekday() == 4:
        if now.hour >= 16:
            message = "Biertijd!"
            #return {"message": "Biertijd!"}
        else:
            s2 = '16:00'
            diff = datetime.datetime.strptime(s2, '%H:%M') - datetime.datetime.strptime(s1, '%H:%M')
            hours = int(diff.seconds // (60 * 60))
            mins = int((diff.seconds // 60) % 60)
            message = "Geen biertijd, nog "+str(hours)+" uur en "+str(mins)+" minuten"
            #return {"message": "Geen biertijd, nog "+str(hours)+" uur en "+str(mins)+" minuten"}
    elif datetime.datetime.today().weekday() in [5,6]:
        if now.hour > 14:
            message = "Biertijd!"
            #return {"message": "Biertijd!"}
        else:
            s2 = '14:00'
            diff = datetime.datetime.strptime(s2, '%H:%M') - datetime.datetime.strptime(s1, '%H:%M')
            hours = int(diff.seconds // (60 * 60))
            mins = int((diff.seconds // 60) % 60)
            message = "Geen biertijd, nog "+str(hours)+" uur en "+str(mins)+" minuten"
            #return {"message": "Geen biertijd, nog "+str(hours)+" uur en "+str(mins)+" minuten"}
    else:
        message = "Geen biertijd! :cry:"

    fields = SectionBlock(fields=[message])
    block = Block()
    print(fields)
    #block = {"blocks": [fields]}
    return block

@app.post("/tijdvoorbier")
async def post_slack():
    return slack_payload()

@app.get("/tijdvoorbier")
async def post_slack():
    return slack_payload()
