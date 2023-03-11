## 1. 케이스 별 A+B 추가시키기

case = int(input())
for i in range(case):
    data = input().split(" ")
    a = int(data[0])
    b = int(data[1])
    print("Case #%d: %d" % (i+1,a+b))

