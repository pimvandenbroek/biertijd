from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/tijdvoorbier")
async def root():
    now = datetime.datetime.now()
    s1 = str(now.hour)+":"+str(now.minute)
    if datetime.datetime.today().weekday() == 4:
        if now.hour >= 16:
            return {"message": "Biertijd!"}
        else:
            s2 = '16:00'
            diff = datetime.datetime.strptime(s2, '%H:%M') - datetime.datetime.strptime(s1, '%H:%M')
            hours = int(diff.seconds // (60 * 60))
            mins = int((diff.seconds // 60) % 60)
            return {"message": "Geen biertijd, nog "+str(hours)+" uur en "+str(mins)+" minuten"}
    elif datetime.datetime.today().weekday() in [5,6]:
        if now.hour > 14:
            return {"message": "Biertijd!"}
        else:
            s2 = '14:00'
            diff = datetime.datetime.strptime(s2, '%H:%M') - datetime.datetime.strptime(s1, '%H:%M')
            hours = int(diff.seconds // (60 * 60))
            mins = int((diff.seconds // 60) % 60)
            return {"message": "Geen biertijd, nog "+str(hours)+" uur en "+str(mins)+" minuten"}
    else:
        return {"message": "Geen biertijd!"}