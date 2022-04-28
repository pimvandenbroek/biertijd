from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import datetime
import random

def create_application() -> FastAPI:
    application = FastAPI(
        title='Slack API',
        version='0.1',
        contact={
            "name": "pimvandenbroek",
            "url": "https://github.com/pimvandenbroek/tijdvoorbier",
        },
        debug=True,
        docs_url='/docs',
        redoc_url='/redoc',
        #root_path='/slack'
    )

    @application.get('/health', include_in_schema=False)
    def health():
        return {'Message': 'OK'}

    return application


app = create_application()

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
        image_list = [
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaMgaIVdPn2WqkMEQ_EplU8dbTzH02ljf7KQ&usqp=CAU',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8mRKQiMPr_0gRraSq2nJ6zvBOlC5DY4oOcg&usqp=CAU',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpW-72LbUhjNhY8QVYkMT7G3TyBIWFXs2QkA&usqp=CAU'
            ]
    if(image=='yay'):
        image_list = [
            'https://st2.depositphotos.com/2969793/5450/i/450/depositphotos_54506511-stock-photo-people-drinking-beer-in-a.jpg',
            'https://media.istockphoto.com/photos/asian-friends-drinking-beer-outdoors-at-the-brewery-for-the-new-year-picture-id1287133941?b=1&k=20&m=1287133941&s=170667a&w=0&h=1SKXAifNNm4KNI4_BENOJDs1VFmY2Y5LNMpUtIrGtKs=',
            'https://img.freepik.com/free-photo/cheers-group-beer-mug-young-men-brew-beer-glasses-celebrate-their-success_61243-130.jpg?w=2000',
            'https://www.dehorecabazaar.nl/_Files_Pagecontent/1216-no-title.jpg']
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
