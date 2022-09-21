#완전제곱수
# 입력 받은 값 사이의 완전제곱수 구하기

num1 = int(input())
num2 = int(input())

PSN = [] # 완전제곱수를 저장하는 배열

for i in range(num1,num2+1):
    root = int(i**0.5) # i 값을 루트 값으로 바꿈
    if i == root **2: # i 값과 루트의 제곱이 같으면
        PSN.append(i) # 완전제곱수 배열에 추가

if len(PSN) == 0: # PSN이 비어 있으면 -1 출력
    print(-1)
else:
    print("{0} \n{1}".format(sum(PSN),min(PSN))) #배열의 합과 최솟값 출력


