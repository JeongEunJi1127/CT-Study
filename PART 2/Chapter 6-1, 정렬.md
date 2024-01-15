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


### :two: 위에서 아래로
> 하나의 수열에는 다양한 수가 존재한다. 수는 크기에 상관없이 나열되어 있다. 이 수를 큰 수부터 작은 수의 순서로 정렬해야 한다. 수열을 내림차순으로 정렬하는 프로그램을 만드시오.  

:speech_balloon: 입력을 받아 리스트에 저장 후 sort()나 sorted() 함수 사용  
:thought_balloon: [풀이](https://github.com/JeongEunJi1127/Algorithm/blob/master/%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%20%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4/Chapter%206%20%EC%A0%95%EB%A0%AC/%EC%9C%84%EC%97%90%EC%84%9C%20%EC%95%84%EB%9E%98%EB%A1%9C.py)

### :three: 성적이 낮은 순서로 학생 출력하기
> N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다. 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하시오.

:speech_balloon: 딕셔너리에 학생 정보를 짝을 이뤄서 저장 후 sorted() 함수와 lambda 함수를 이용하여 key = array[1], reverse = True 로 정렬한다.   
:thought_balloon: [풀이](https://github.com/JeongEunJi1127/Algorithm/blob/master/%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%20%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4/Chapter%206%20%EC%A0%95%EB%A0%AC/%EC%84%B1%EC%A0%81%EC%9D%B4%20%EB%82%AE%EC%9D%80%20%EC%88%9C%EC%84%9C%EB%A1%9C%20%ED%95%99%EC%83%9D%20%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0.py)

### :four: 두 배열의 원소 교체
> 두 개의 배열 A,B 는 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수이다. 동빈이는 최대 K번 배열 A,B에 있는 원소를 하나씩 골라서 두 원소를 서로 바꾸는 연산을 수행할 수 있다. 동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이다.

:speech_balloon: 배열 A에 있는 가장 작은 원소를 골라 배열 B에 있는 가장 큰 원소와 바꾸면 된다. 단, 배열 A에 있는 가장 작은 원소가 배열 B의 가장 큰 원소보다 작아야만 교체해야 한다.  
:thought_balloon: [풀이](https://github.com/JeongEunJi1127/Algorithm/blob/master/%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%20%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4/Chapter%206%20%EC%A0%95%EB%A0%AC/%EB%91%90%20%EB%B0%B0%EC%97%B4%EC%9D%98%20%EC%9B%90%EC%86%8C%20%EA%B5%90%EC%B2%B4.py)
