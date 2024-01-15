## `Chapter 6` 정렬

### :one: 기준에 따라 데이터를 정렬
- 정렬 : 데이터를 특정한 기준에 따라서 순서대로 나열  
- 리스트를 뒤집는 연산의 시간복잡도 : O(N)

#### 선택 정렬
- 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번재 데이터와 바꾸는 과정  
- 선택 정렬의 시간복잡도 : O(N^2)     
->  매우 비효율적 !!

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    # 두 변수의 위치를 swap 하는 방법
    array[i], array[min_index] = array[min_index], array[i] 
```

#### 삽입 정렬
- 특정한 데이터를 적절한 위치에 삽입  
- 두 번째 데이터부터 정렬
- 특정 데이터의 왼쪽에 있는 데이터들은 이미 정렬이 된 상태이므로 자기보다 작은 데이터를 만나면 바로 그 오른쪽에 삽입하면 됨
- 삽입 정렬의 시간복잡도 : O(N^2)   
 ->  `데이터가 거의 정렬되어 있는 최선의 경우` 퀵정렬 보다 빠르고 O(N) 의 시간복잡도 가짐

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in ragne(1,len(array)):
    for j in range(i,0,-1):
        if array[j-1] > array[j]:
            array[j-1] , array[j] = array[j], array[j-1]
        # 자기보다 작은 데이터를 만나면 바로 멈춤
        else:
            break
```

#### 퀵 정렬
- 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 동작
- `호어 분할 방식`   
-> 리스트에서 첫번째 데이터를 피벗(기준)으로 정한다   
-> 왼쪽에서부터 피벗보다 큰 데이터를, 오른쪽에서부터 피벗보다 작은 데이터를 찾는다.
-> 큰 데이터와 작은 데이터의 위치를 서로 교환
- 퀵 정렬의 시간복잡도  : O(NlogN)   
  -> 삽입 정렬과 달리 데이터가 거의 정렬되어 있는 최악의 경우 시간복잡도가 O(N^2) 이다

```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array,start,end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
         # 엇갈릴 경우 작은 데이터와 피벗 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았을 경우 작은 데이터와 큰 데이터 교체
        else:
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽, 오른쪽 부분 수행
    quick_sort(array,start,right-1)
    quick_sort(array,right,end-1)

quick_sort(array,0,len(array)-1)
print(array)

```

#### 계수 정렬
- 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있다는 조건이 부합할 때만 사용 가능
- 모든 범위를 담을 수 있는 크기의 리스트를 선언
- `동일한 값을 가지는 데이터가 여러 개 등장할 때 효율적`
- 계수 정렬의 시간복잡도 : O(N+K) (K는 데이터 중 최대값)  


```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(array)+1)

for i in array:
    count[i] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')

```

#### 파이썬의 정렬 라이브러리
- sorted()  
 -> 병합 정렬 (퀵 정렬과 동작 방식이 비슷) 기반으로 만들어짐   
 -> O(NlogN)의 시간복잡도 가짐 
- sort()  
 -> 리스트 객체의 내장 함수  
 -> O(NlogN)의 시간복잡도 가짐