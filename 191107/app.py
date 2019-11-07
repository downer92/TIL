from flask import Flask, render_template, request
import random
import requests
from pprint import pprint


app = Flask(__name__)

@app.route('/')
def hello():
    name = "World!!"
    return f'Hello {name}!'

@app.route('/mulcam')
def mulcam():
    return 'Hello mulcam'

@app.route('/greeting/<string:name>') # 어떤 이름으로 변수를 받을지
def greeting(name):
    return f'{name}님 안녕하세요.'

# 인원수만큼 점심메뉴 추천해주는 기능 만들기~
@app.route('/lunch/<int:num>')
def lunch(num):
    menu=["짜장면", "짬뽕", "라면", "스테이크", "삼겹살", "초밥"]
    order = random.sample(menu, num)
    return render_template('menu.html', menu=order)

# 실습 : /lotto를 입력 받으면 6개의 수 추천
@app.route('/lotto')
def lotto():
    random_num = random.sample(range(1, 46), 6)
    return str(random_num)

@app.route('/html')
def html():
    multiline = '''
    <h1> This is h1 tag </h1>
    <p> This is p tag </p>
    <div style="background-color: red; width: 100px; height: 100px;"> </div>
    '''
    return multiline

@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html', name=name) #템플릿 파일을 로드할 때 이런식으로 사용.


@app.route('/fake_naver')
def fake_naver():
    return render_template('fake_naver.html')

# 구글로 검색창 만들기 실습
@app.route('/fake_google')
def fake_google():
    return render_template('fake_google.html')

@app.route('/send')
def send():
    return render_template('send.html')

@app.route('/receive')
def receive():
    name = request.args.get('name') # arguements 안에서 name이라는 이름을 가진 애를 받아오겠다
    message = request.args.get('message')
    return render_template('receive.html', name=name, msg=message)

# 인디언 이름짓기 시습
@app.route('/indian_send')
def indian_send():
    return render_template('indian_send.html')

@app.route('/indian_receive')
def indian_receive():
    name=request.args.get('name')
    name1=["말 많은", "시끄러운", "어두운", "적색", "조용한", "웅크린", "백색", "지혜로운", "용감한", "날카로운", "욕심많은"]
    name2=["늑대", "태양", "양", "매", "황소", "불꽃", "나무", "달빛", "말", "돼지", "하늘","바람"]
    name3=["와(과) 함께 춤을", "의 기상", "은(는) 그림자 속에", "의 환생", "의 죽음", "아래에서", "를(을) 보라", "이(가) 노래하다", "의 그림자",
    "의 일격", "에게 쫓기는 남자", "의 행진", "의 왕", "의 유령", "를(을) 죽인자"]

    random1 = random.choice(name1)
    random2 = random.choice(name2)
    random3 = random.choice(name3)
    
    random_name = random1+random2+random3

    return render_template('indian_receive.html', name=random_name)

@app.route('/lotto_get')
def lotto_get():
    return render_template('lotto_get.html')

@app.route('/lotto_num')
def lotto_num():
    num = request.args.get("num")
    url = f"https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}"
    res = requests.get(url).json() # json형태로 변환
    
    # [받는변수 for 받는변수 in 범위데이터]
    wnum = [ res[f'drwtNo{i}'] for i in range(1, 7)]
    lotto = random.sample(range(1, 46), 6)

    match = list(set(wnum) & set(lotto))
    
    count = len(match)
    if count==6 :
        word = '축하합니다. 1등에 당첨되셨습니다!!'
    if count==5 :
        word = '축하합니다. 2등이십니다!!'
    if count==4 :
        word = '축하합니다. 3등이십니다~~'
    if count==3 :
        word = '축하해 4등이야^^'
    else :
        word = '넌 꽝이야^^'
    return render_template('lotto_result.html', num=num, wnum=wnum, lotto=lotto, word=word)


if __name__ == "__main__":
    app.run(debug=True, port=8000)