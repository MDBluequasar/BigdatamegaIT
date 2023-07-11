a = 2
b = 1
n = 20 



# result = 0
# add = 0
# while True:
#   if n // a != 0:
#     add = (n // a) * b
#     result += add
#     n = n % a + add
#   else:
#     break
# print(result) 

s = n % a
print(s)

# 푸드 파이터
def solution(food):
    #좌측 문자열을 구한뒤,
    #좌측 문자열 + '0' + 리버스(좌측문자열)
    #이러면 될듯?
    
    #파이썬은 문자열도 곱연산이 되서 좀더 편하긴 할듯
    answer = ''
    left = ''
    for idx, x in enumerate(food):
        # print(idx)
        # print(x)
        if idx == 0:
            continue
        left+= str(idx)*(x//2)
    answer = left + '0' + left[::-1]
    return answer

# 추억 점수
def solution(name, yearning, photo):
    #name yearning 둘을 key value로 하는 해쉬맵 쓰면 될듯?
    dic = {}
    answer = []
    #dic 내용 주입
    for idx, x in enumerate(name):
        dic[x] = yearning[idx]
    #scoring
    for e in photo:
        score = 0
        for s in e:
            if s in dic:
                score += dic[s]
        #append answer list
        answer.append(score)
    return answer