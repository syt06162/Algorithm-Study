# 구간합 계산. 
# prefix_sum = [0] 에서 시작
# L 부터 R 까지 합은 P[R] - P[L-1] (단 배열이 1부터 시작한다 가정)

N = 5 # 데이터 개수
data = [10, 20, 40, 50, 70]

prefix_sum = [0]
sum_value = 0

for i in range(N):
    sum_value += data[i]
    prefix_sum.append(sum_value)

# 만약 2번째부터 4번째 (즉 20 40 50)의 합을 출력하고 싶은 경우
left = 2
right = 4
print(prefix_sum[right] - prefix_sum[left-1])