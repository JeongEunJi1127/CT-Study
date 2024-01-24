## `Appendix A`, 코딩테스트를 위한 파이썬 문법

### :five: 입출력

- 파이썬에서 데이터를 입력받을 떄는 *input()* 을 이용
- 데이터가 공백으로 구분되는 경우 *list(map(int,input().split()))* 을 이용

- 입력을 최대한 빠르게 받아야 하거나 많은 수의 데이터가 입력되는 경우 *sys.stdin.readline()* 함수를 이용한다

```
import sys
sys.stdin.readline().rstrip()
# rstrip() : 줄 바꿈 기호 제거
```

### :six: 주요 라이브러리의 문법와 문제점

#### 표준 라이브러리

- 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리
- 파이썬 표준 라이브러리 주소 -> *https://docs.python.org/ko/3/library/index.html*

**1. 내장 함수**
- import 명령어 없이 바로 사용할 수 있는 함수
- input(), print(), sum(), min(), max(), eval() (수식이 문자열로 들어오면 계산한 결과를 반환) , sorted() 

**2. itertools**
- iterable 형태의 데이터 (리스트, 사전 자료형, 튜블 자료형) 를 처리하는 기능 제공
- 클래스 이므로 객체 초기화 이후 리스트 자료형으로 변환
- permutations (순열)
    - iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산
        ```
        from itertools import permutaitons

        data = ["a", "b", "c"]
        result = list(permutaitons(data,3)) 
        ```

- combinations (조합)
    - iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산
        ```
        from itertools import combinations

        data = ["a", "b", "c"]
        result = list(combinations(data,3)) 
        ```

- product
    - iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산, 단 원소는 중복하여 뽑음
        ```
        from itertools import product

        data = ["a", "b", "c"]
        result = list(product(data, repeat=2))
        ```

**3. heapq**
- 힙(Heap) 기능 제공
- 우선순위 큐 기능을 구현하기 위해 사용
- heap1.heappush(), heap1.heappop()
- 파이썬에서는 최대 힙을 제공 X

**4. bisect**
- 이진탐색 기능 제공
- *정렬된 배열* 에서 특정한 원소를 찾아야 할 때 효과적
- bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
- bisect_right(a, x) : 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

**5. collections**
- deque
    - 큐를 구현
    - 인덱싱, 슬라이싱 사용할 수 없음
    - 리스트는 원소를 추가하거나 제거할 때 *가장 뒤쪽 원소* 를 기준으로 수행   
      deque 사용하면 데이터의 시작이나 끝 부분에 접근하기 쉬움

    - 시간복잡도 비교

    ||리스트|deque|
    |------|---|---|
    |가장 앞쪽에 원소 추가|O(N)|O(1)
    |가장 뒤쪽에 원소 추가|O(1)|O(1)
    |가장 앞쪽에 있는 원소 제거|O(N)|O(1)
    |가장 뒤쪽에 있는 원소 제거|O(1)|O(1)

    - 첫 번째 원소 제거 popleft()  
    첫 번째 원소 삽입 appendleft()  
    마지막 원소 제거 pop()  
    마지막 원소 삽입 append()
      

- Counter  
    - iterable 객체 내의 원소 등장 횟수를 세는 기능 제공



**6. math**
- 수학 기능을 제공하는 라이브러리
- 팩토리얼(factorial(x)), 제곱근(sqrt(x)), 최대공약수(gcd(a,b)) 
- 삼각함수, 파이와 같은 상수 제공