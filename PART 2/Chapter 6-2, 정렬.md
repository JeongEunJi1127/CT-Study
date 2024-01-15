## `Chapter 6` 정렬

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
