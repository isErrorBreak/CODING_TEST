#첼시를 도와줘!

N = int(input())

for _ in range(N):
    Case = int(input())
    Chelsea = {} #  첼시 선수의 이름과 가격
    for _ in range(Case):
        price, player = input().split()
        Price = int(price) # price의 자료형을 int로 바꿈
        Chelsea[Price] = player #Chelsea에 Price를 키로 갖고 player를 value로 갖는 dict를 생성
    print(Chelsea.get(max(Chelsea.keys()))) # 키값의 최대값의 value를 출력함.