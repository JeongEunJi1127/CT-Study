## `Chapter 6` 정렬

### :one: 기준에 따라 데이터를 정렬
- 정렬 : 데이터를 특정한 기준에 따라서 순서대로 나열  
- 리스트를 뒤집는 연산의 시간복잡도 : O(N)

#### 선택 정렬
- 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번재 데이터와 바꾸는 과정  
- 선택 정렬의 시간복잡도 : O(N^2) ->  매우 비효율적 !!

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 두 변수의 위치를 swap 하는 방법
```

#### 삽입 정렬
- 특정한 데이터를 적절한 위치에 삽입  
- 특정 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다. (두 번째 데이터부터 시작한다)  
- 삽입 정렬의 시간복잡도 : O(N^2) ->  데이터가 거의 정렬되어 있는 최선의 경우 O(N) 의 시간복잡도 가짐

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in ragne(1,len(array)):
    for j in range(i,0,-1)
```