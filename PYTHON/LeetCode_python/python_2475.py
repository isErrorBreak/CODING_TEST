#검증수

num = list(map(int, input().split())) # 고유번호를 입력받음
sqr_num = [] # 제곱한 값을 넣는 리스트
for i in num:
    sqr_num.append(i**2)

number_of_verifications = sum(sqr_num)%10 # 검증수 구하기
print(number_of_verifications)

