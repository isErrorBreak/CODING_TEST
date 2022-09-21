#평균
N = int(input())

subject = list(map(int,input().split()))

m_subject = max(subject) # 리스트 중 최대값
f_sum = 0 # 변경된 값의 합을 저장
for i in subject: #리스트 길이 만큼 반복
    f_sum += i/m_subject*100 #변경된 합을 구하는 식

f_avg = f_sum/N # 과목수만큼 나눔

print(float(f_avg))

