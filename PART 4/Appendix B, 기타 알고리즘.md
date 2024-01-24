## `Appendix B`, 기타 알고리즘

### :one: 소수의 판별
- 소수 : 2보다 큰 자연수 중 1과 자기 자신을 제외한 자연수로는 나누어 떨어지지 않는 자연수

```python
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```
- `하나의 수` n이 소수인지 판별하는 함수
- 시간 복잡도 : O(N)

```python
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
```
- 개선된 소수 판별 함수
- 예시) 8의 약수  
    1 * 8 = 8  
    2 * 4 = 8  
    4 * 2 = 8  
    8 * 1 = 8  
    : 다음과 같이 가운데 약수를 중심으로 각 등식이 대칭이다. 따라서 특정 수가 소수인지 확인할 때 `가운데 약수까지만` 나누어 떨어지는지 확인하면 됨

- 시간 복잡도 : O(N^1/2)

### :two: 에라토스테네스의 채
- `여러개의 수`가 소수인지 판별할 때 사용하는 알고리즘
- 에라토스테네스의 채 알고리즘의 시간 복잡도 : O(NloglogN)
> 1. 2부터 N까지의 모든 자연수 나열
> 2. 남은 수 중 아직 처리하지 않은 가장 작은 수 i 찾기
> 3. 남은 수 중 i의 배수 모두 제거 (i는 제거 X)
> 4. 더 반복할 수 없을 때까지 2, 3번 반복

```python
import math

n = 1000
array = [True for i in range(i+1)]

# 에라토스테네스의 채 알고리즘
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
for i in range(2, n+1):
    if array[i]:
        print(i, end=" ")
```
### :three: 투 포인터
- 투 포인터 : 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하며 처리

<br>

- `특정한 합을 가지는 부분 연속 수열` 투 포인터로 찾는 방법
> 1. 시작점과 끝점이 인덱스 0을 가리킴
> 2. 현재 부분합이 M과 같으면 카운트
> 3. 현재 부분합이 M보다 크거나 같으면 시작점 1 증가
> 4. 현재 부분합이 M보다 작으면 끝점 1 증가
> 5. 2 ~ 4번 과정 반복

<br>

- `정렬되어 있는 두 리스트의 합집합` 투 포인터로 찾는 방법
> 1. 정렬된 리스트 A, B를 입력받는다
> 2. 리스트 A에서 처리되지 않은 원소 중 가장 작은 원소를 i가 가리키도록 한다
> 3. 리스트 B에서 처리되지 않은 원소 중 가장 작은 원소를 j가 가리키도록 한다
> 4. A[i], B[j] 중 더 작은 원소를 결과 리스트에 담는다
> 5. 2 ~ 4번 과정 반복

### :four: 구간 합 계산
- 연속된 N개의 수가 있을 때, 특정 구간의 모든 수를 합한 값을 구하는 문제
- 접두사 합을 이용한 구간 합 계산 시간복잡도 (N개의 데이터, M개의 구간):  O(N + M)
- 접두사 합 : 리스트의 맨 앞부터 특정 위치까지의 합
> 1. N개의 수에 대해 접두사 합 배열 P를 구해놓는다
> 2. 매 구간(l,r)을 확인할 때, 구간 합은 P[r] - P[l-1]
```python
data = [10, 20, 30, 40, 50]
sum = 0
# 접두사 합 저장할 리스트
prefix_sum = [0]
answer = 0

for i in data:
    sum += i
    prefix_sum.append(sum)
# 구간 (3,4)의 합
print(prefix_sum[4] - prefix_sum[3-1])
```

### :five: 순열과 조합
- 순열 
    - 서로 다른 n개에서 r개를 선택하여 일렬로 나열하는 것
    - n! / (n - r)!
    - itertools.permutations(data,n)
- 조합 
    - 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것
    - n! / r! * (n - r)!
    - itertools.combinations(data,n)
