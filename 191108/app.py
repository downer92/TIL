from flask import Flask, render_template, request
import random
import requests
from decouple import config
from pprint import pprint

app=Flask(__name__)

token=config('TOKEN') #decouple library를 활용하여 .env의 token 값을 불러온다.
base_url = f"https://api.telegram.org/bot{token}"


@app.route('/telegram')
def telegram():
    # token=config('TOKEN')
    # base_url = f"https://api.telegram.org/bot{token}"
    res = requests.get(f'{base_url}/getUpdates').json()
    #pprint(res) #요청된 json 확인
    chat_id = res['result'][0]['message']['chat']['id'] #get chat id from json

    #lotto 번호 보내기
    lotto = random.sample(range(1,47), 6)
    sendMessage = f'{base_url}/sendMessage?chat_id={chat_id}&text={lotto}'
    send_res = requests.get(sendMessage).json()
    get_lotto = send_res['result']['text']

    return f'추천 로또 번호 : {get_lotto}'

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/send_msg')
def send_msg():
    req = request.args.get('chat')
    res = requests.get(f'{base_url}/getUpdates').json()
    print(res)
    chat_id = res['result'][0]['message']['chat']['id']
    print(chat_id)
    sendMessage = f'{base_url}/sendMessage?chat_id={chat_id}&text={req}'
    requests.get(sendMessage).json()
    return '보내기 완료'

@app.route('/', methods=['POST'])
def tel_wh():
    req =  request.get_json().get('message')
    #print(req['chat']['id'],req['text'])
    if req is not None:
        chat_id=req.get('chat').get('id')
        text=req.get('text')
    print(chat_id, text)
    if text == '로또':
        #pprint(req)
        lotto = random.sample(range(1,47), 6)
        sendMessage = f'{base_url}/sendMessage?chat_id={chat_id}&text={lotto}'
        requests.get(sendMessage).json()
    
    if '/인디안' in text :
        name1=["말 많은", "시끄러운", "어두운", "적색", "조용한", "웅크린", "백색", "지혜로운", "용감한", "날카로운", "욕심많은"]
        name2=["늑대", "태양", "양", "매", "황소", "불꽃", "나무", "달빛", "말", "돼지", "하늘","바람"]
        name3=["와(과) 함께 춤을", "의 기상", "은(는) 그림자 속에", "의 환생", "의 죽음", "아래에서", "를(을) 보라", "이(가) 노래하다", "의 그림자",
        "의 일격", "에게 쫓기는 남자", "의 행진", "의 왕", "의 유령", "를(을) 죽인자"]
        random1 = random.choice(name1)
        random2 = random.choice(name2)
        random3 = random.choice(name3)
        random_name = random1+random2+random3
        sendMessage = f'{base_url}/sendMessage?chat_id={chat_id}&text={random_name}'
        requests.get(sendMessage).json()

    if '/번역' in text :
        replace_text = text.replace("/번역", "") 
        C_ID = config('C_ID')
        C_SC = config('C_SC')
        url = "https://openapi.naver.com/v1/papago/n2mt"

        headers = {
          "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
          "X-Naver-Client-Id" : C_ID,
          "X-Naver-Client-Secret" : C_SC
        }

        data = {
            "source" : "ko",
            "target" : "en",
            "text" : replace_text
        }
        
        req = requests.post(url, headers=headers, data=data).json()
        sending_text = req.get('message').get('result').get('translatedText')
        sendMessage = f'{base_url}/sendMessage?chat_id={chat_id}&text={sending_text}'
        requests.get(sendMessage).json()
        
    return '',200



@app.route('/papago')
def papago() :
    C_ID = config('C_ID')
    C_SC = config('C_SC')
    url = "https://openapi.naver.com/v1/papago/n2mt"

    headers = {
      "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
      "X-Naver-Client-Id" : C_ID,
      "X-Naver-Client-Secret" : C_SC
    }

    data = {
        "source" : "ko",
        "target" : "en",
        "text" : "안녕하십니까?"
    }

    req = requests.post(url, headers=headers, data=data).json()

    pprint(req)

    return "Finished"

if __name__ == "__main__":
    app.run(debug=True) 