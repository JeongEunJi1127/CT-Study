## `Appendix C`, 개발형 코딩 테스트

### :one: 개발형 코딩 테스트에 필요한 지식
#### 알고리즘 코딩 테스트 VS 개발형 코딩 테스트 
||알고리즘 코딩 테스트|개발형 코딩 테스트 |
|---|---|---|
|목적|정해진 시간 안에 동작하는 효율적인 프로그램 작성|정해진 목적에 따라 동작하는 완성된 프로그램 개발|
|개발할 것|요구 사항에 맞게 효율적으로 동작하는 모듈 개발|모듈을 적절히 조합하여 완성도 높은 프로그램 개발|
|풀이 시간 & 코드의 길이|짧다 |길다|

- 자신의 직무와 관련된 개인 프로젝트 시작하여 대비!

#### 서버와 클라이언트
- 클라이언트
    - 정보를 요청하는 측 
    - 요청 : 서버로 데이터를 보내는 것
    - *서버로 요청 보냄 -> 응답 기다림 -> 응답 오면 화면에 출력*
    - 게임의 경우 PC(클라이언트)에 게임 배경이나 캐릭터는 미리 저장되어 있고, 게임 플레이 도중 서버로부터 데이터(귓속말, 서버의 원할함 등)를 받아 내 게임 정보를 재구성해 화면에 출력한다
- 서버
    - 클라이언트에 서비스를 제공해주는 컴퓨터
    - *클라이언트로부터 요청 받음 -> 응답 보냄*
    - 서버 프로그램 : 클라이언트에 서비스를 제공하기 위해 서버가 실행하는 프로그램  
        - 게임 개발의 서버 프로그램 : c++, c#, go
        - 웹, 모바일의 서버 프로그램 : 자바스크립트, 파이썬 등
- 파이썬으로 웹 요청
    - HTTP : 웹상에서 데이터를 주고받기 위한 프로토콜
