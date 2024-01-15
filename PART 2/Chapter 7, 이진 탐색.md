## `Chapter 7` 이진 탐색

### :one: 범위를 반씩 좁혀가는 탐색

#### 순차 탐색
- 리스트 안에 있는 특정 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법.
- 최악의 시간복잡도 : O(N)

#### 이진 탐색
- 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있음
- 반으로 쪼개면서 탐색, (시작점, 끝점, 중간점) 변수 사용 
- 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교
- 탐색 범위가 1000만이 넘어가면 이진탐색과 같이 시간복잡도가 O(logN)인 알고리즘을 선택해야 풀 수 있음을 기억하자
- 시간복잡도 : O(logN)
<br>

- 재귀 함수를 이용한 이진 탐색 구현
```python
def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start+end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

n, target = list(map(int,input().split()))
array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)
```

- 반복문을 이용한 이진 탐색 구현
```python
def binary_search(array,target,start,end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[min] > target:
            end = mid - 1
        else:
            start = mid + 1

n, target = list(map(int,input().split()))
array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)
```

#### 트리 자료구조
- 노드와 노드의 연결
- 노드 : 정보를 가지고 있는 개체
- 트리 자료구조의 특징  
> 1. 트리는 부모 노드와 자식 노드로 표현
> 2. 루트 노드 : 트리의 최상단 노드
> 3. 단말 노드 : 트리의 최하단 노드
> 4. 트리에서 일부 노드를 떼어내도 트리 구조이며 이를 서브 트리라고 한다
> 5. 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다

#### 이진 탐색 트리
- 이진 탐색이 동작 할 수 있도록 고안된 효율적인 탐색이 가능한 자료구조
- 이진 탐색 트리의 특징
> 1. 부모 노드보다 왼쪽 자식노드가 작다
> 2. 부모 노드보다 오른쪽 자식 노드가 크다

#### 파라메트릭 서치 유형
- 최적화 문제를 결정 문제 (예, 아니오로 답하는 문제)로 바꾸어 해결하는 기법
- 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에 주로 사용

### :two: 부품 찾기
> 부품의 개수는 N개 이고 각 부품은 고유 정수 번호가 있다. 손님이 M개 종류의 부품을 대량 구매 하고자 할 때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자

:speech_balloon: 매장의 부품을 정렬한 후 이진 탐색을 이용하여 손님이 요청한 부품 번호가 있는지 탐색한다     
:thought_balloon: [풀이](https://github.com/JeongEunJi1127/Algorithm/blob/master/%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%20%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4/Chapter%207%20%EC%9D%B4%EC%A7%84%20%ED%83%90%EC%83%89/%EB%B6%80%ED%92%88%20%EC%B0%BE%EA%B8%B0.py)

### :three: 떡볶이 떡 만들기
> 동빈이네 떡볶이 떡은 길이가 일정하지 않다. 절단기에 높이 H를 지정하면 떡을 한 번에 절단한다. 손님이 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하시오.

:speech_balloon: 파라메트릭 서치 유형의 문제. '현재 이 높이로 자르면 조건을 만족할 수 있는가?'를 확인한 뒤 조건의 만족 여부에 따라 탐색 범위를 좁혀서 해결할 수 있다.   
:thought_balloon: [풀이](https://github.com/JeongEunJi1127/Algorithm/blob/master/%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%20%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4/Chapter%207%20%EC%9D%B4%EC%A7%84%20%ED%83%90%EC%83%89/%EB%96%A1%EB%B3%B6%EC%9D%B4%20%EB%96%A1%20%EB%A7%8C%EB%93%A4%EA%B8%B0.py)