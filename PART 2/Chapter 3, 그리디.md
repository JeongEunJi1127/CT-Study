## `Chapter 3` 그리디

### :one: 그리디 알고리즘
- 현재 상황에서 지금 당장 좋은 것만 고르는 방법

#### :grey_exclamation: 예제 - 거스름돈

>거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정  
손님에게 거슬러 주어야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하여라  
 (단, 거슬러 줘야 할 돈 N은 항상 10의 배수)  
 
:speech_balloon: 가장 큰 화폐 단위부터 돈을 거슬러 준다  
:thought_balloon: [풀이](https://github.com/JeongEunJi1127/Algorithm/blob/master/%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%20%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4/Chapter%203%20%EA%B7%B8%EB%A6%AC%EB%94%94/%EA%B1%B0%EC%8A%A4%EB%A6%84%EB%8F%88.py)

- 그리디 알고리즘의 정당성  
: 그리디 알고리즘으로 문제의 해법을 찾았을 떄는 그 해법이 정당한지 검토해야 한다  
: 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토할 수 있어야 함

### :two: 큰 수의 법칙
> 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만들어보자  
단, 배열의 특정 인덱스에 해당하는 수가 연속해서 K번 초과하여 더해질 수는 없다

:speech_balloon: 입력값 중 가장 큰 수를 K번 더하고 두번째로 큰 수를 한 번 더하는 연산을 반복   
:thought_balloon: [풀이](https://github.com/JeongEunJi1127/Algorithm/blob/master/%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%20%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4/Chapter%203%20%EA%B7%B8%EB%A6%AC%EB%94%94/%ED%81%B0%20%EC%88%98%EC%9D%98%20%EB%B2%95%EC%B9%99.py)

