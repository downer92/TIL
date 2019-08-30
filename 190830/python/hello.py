# ctrl + n 새 파일
# cyrl + s hello.py
print('happy hacking!')

name = '하진'
print(name)

name = 123
print(name)

name = True
print(name)

# 리스트
my_list = ['하진', 123, True, '하이']
type(my_list) #type() : 타입을 알아보는 함수
print(my_list[0])

#딕셔너리(해시) : 키랑 밸류로 이루어진!
my_dict = {'하진': 28, '홍길동': 600}
print(my_dict['하진'])
print(my_dict['홍길동'])

# 조건
a = 5
if a>0:
    print('양수')
else:
    print('음수')


#반복
a = [1, 3, 5, 6]
for num in a:
    print(num)

name = '홍길동'
for char in name:
    print(char)