from django.db import models

# Create your models here.
class Board(models.Model): # models의 Model을 상속 받아서 만든다.
    title = models.CharField(max_length=10) # 캐릭터 필드는 max_length로 최대 길이를 설정해줘야 한다.
    content = models.TextField() # 텍스트 필드에도 max_length를 줄 수 있는데 DB에 적용이 되는 것이 아니고 외부에서 글자 제한으로 보여질 뿐임!
    created_at = models.DateTimeField(auto_now_add=True) # 날짜 데이터는 데이트 타임 필드로! auto_now_add는 해당 데이터가 DB에 저장이 될 때 저장이 되는 시간을 created_at에 자동으로 넣어주는 기능
    # 장고에서는 pk로 쓰는 id가 자동으로 생성이 된다. 따라서 우리는 컬럼명에 주로 신경쓰면 된다!
    updated_at = models.DateTimeField(auto_now=True) # 데이터 수정 시간에 대한 컬럼 추가. 데이터 수정 시점에 맞춰서 자동으로 데이터를 업데이트 하기 위해 auto_now=True 옵션을 추가한다.

    # query 결과로 리턴되는 object를 보기 쉽게 하기 위해 다음과 같이 메소드 수행
    def __str__(self): # double under bar = 던더ㅋㅋ
        return f'{self.id} : {self.title}'
    # 테이블이 변경된 것이 아니고 메소드만 추가한 것이므로 migration을 따로 적용하지 않아도 괜찮음. but, 커맨드는 다시 실행해야 한다!

class Subway(models.Model):
    name = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now_add=True)
    menu = models.CharField(max_length=30)
    size = models.CharField(max_length=5)
    bread = models.CharField(max_length=15)
    add = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.name}님이 {self.date}에 주문하신 메뉴의 레시피는 다음과 같습니다. (menu : {self.menu}, size : {self.size}, bread : {self.bread}, add : {self.add})'
    
