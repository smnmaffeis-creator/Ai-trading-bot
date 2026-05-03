import time
import requests
import random

TOKEN = "8762868614:AAG8pKICPaM01e2bN77SHx9cJnzZy-KHABE"
CHAT_ID = "1692745498"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def signal():
    assets = ["GOLD", "SILVER", "EURUSD", "OIL", "BTC"]
    asset = random.choice(assets)

    price = round(random.uniform(50, 200), 2)
    score = random.randint(30, 90)

    if score > 80:
        return f"🟢 BUY {asset}\nENTRY {price}\nTP {price+1}\nSL {price-1}\nScore {score}"
    elif score < 40:
        return f"🔴 SELL {asset}\nENTRY {price}\nTP {price-1}\nSL {price+1}\nScore {score}"
    return None

while True:
    msg = signal()
    if msg:
        send(msg)
    time.sleep(60)
