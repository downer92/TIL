# x = int(input())
# print(x)

# for c in "string":
#     print(c)

# for i in range(0, 5):
#     print(i, i**2)


# score = {
#     '수학': 80,
#     '국어': 90,
#     '음악': 100
# }

# total_score = sum(score.values())
# avg = total_score / len(score)
# print(avg)

# score = {
#     "a": {
#         "수학": 80,
#         "국어": 90,
#         "음악": 100
#     },
#     "b": {
#         "수학": 80,
#         "국어": 70,
#         "음악": 80
#     }
# }

# a_avg = sum(score["a"].values())/len(score["a"])
# b_avg = sum(score["b"].values())/len(score["b"])

# avg = (a_avg + b_avg) / 2
# print(avg)

city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9]
}

# 3-1. 도시별 최근 3일의 온도 평균은?
for name, temp in city.items():
    avg_temp = sum(temp) / len(temp)
    print(f'{name} : 평균 기온은 {avg_temp}입니다.')

# 3-2. 위에서 서울은 영상 2도였던 적이 있나요?
A if 조건문 else B  # 조건문이 True면 A가 리턴, false면 B가 리턴됨
print('있습니다.') if 2 in city["서울"] else print('없습니다.')

