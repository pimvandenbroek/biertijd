from email.message import Message
from fastapi import FastAPI
import datetime
import random


app = FastAPI()

def slack_payload():
    now = datetime.datetime.now()
    s1 = str(now.hour)+":"+str(now.minute)
    if datetime.datetime.today().weekday() == 4:
        if now.hour >= 16:
            message = "Biertijd!"
            image = 'yay'
            #return {"message": "Biertijd!"}
        else:
            s2 = '16:00'
            diff = datetime.datetime.strptime(s2, '%H:%M') - datetime.datetime.strptime(s1, '%H:%M')
            hours = int(diff.seconds // (60 * 60))
            mins = int((diff.seconds // 60) % 60)
            message = "Geen biertijd, nog "+str(hours)+" uur en "+str(mins)+" minuten"
            image = 'nay'
            #return {"message": "Geen biertijd, nog "+str(hours)+" uur en "+str(mins)+" minuten"}
    elif datetime.datetime.today().weekday() in [5,6]:
        if now.hour > 14:
            message = "Biertijd!"
            image = 'yay'
            #return {"message": "Biertijd!"}
        else:
            s2 = '14:00'
            diff = datetime.datetime.strptime(s2, '%H:%M') - datetime.datetime.strptime(s1, '%H:%M')
            hours = int(diff.seconds // (60 * 60))
            mins = int((diff.seconds // 60) % 60)
            message = "Geen biertijd, nog "+str(hours)+" uur en "+str(mins)+" minuten"
            image = 'nay'
            #return {"message": "Geen biertijd, nog "+str(hours)+" uur en "+str(mins)+" minuten"}
    else:
        message = "Geen biertijd! :cry:"
        image = 'nay'

    if(image=='nay'):
        image_list = ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaMgaIVdPn2WqkMEQ_EplU8dbTzH02ljf7KQ&usqp=CAU','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8mRKQiMPr_0gRraSq2nJ6zvBOlC5DY4oOcg&usqp=CAU','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpW-72LbUhjNhY8QVYkMT7G3TyBIWFXs2QkA&usqp=CAU']
    if(image=='yay'):
        image_list = ['https://st2.depositphotos.com/2969793/5450/i/450/depositphotos_54506511-stock-photo-people-drinking-beer-in-a.jpg','https://media.istockphoto.com/photos/asian-friends-drinking-beer-outdoors-at-the-brewery-for-the-new-year-picture-id1287133941?b=1&k=20&m=1287133941&s=170667a&w=0&h=1SKXAifNNm4KNI4_BENOJDs1VFmY2Y5LNMpUtIrGtKs=','https://img.freepik.com/free-photo/cheers-group-beer-mug-young-men-brew-beer-glasses-celebrate-their-success_61243-130.jpg?w=2000','data:image/jpeg;base64,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','https://www.dehorecabazaar.nl/_Files_Pagecontent/1216-no-title.jpg']
    img = random.choice(image_list)      
    sectionblock = {}
    sectionblock["type"] = "section"
    sectionblock["text"] = {}
    sectionblock["text"]["text"] = message
    sectionblock["text"]["type"] = "mrkdwn"
    sectionblock["accessory"] = {}
    sectionblock["accessory"]["type"] = "image"
    sectionblock["accessory"]["image_url"] = img
    sectionblock["accessory"]["alt_text"] = "Bier"

    blocks = {}
    blocks["blocks"] = list()
    blocks["blocks"].append(sectionblock)
    return blocks

@app.post("/tijdvoorbier")
async def post_slack():
    return slack_payload()

@app.get("/tijdvoorbier")
async def post_slack():
    return slack_payload()