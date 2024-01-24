def solution(s):
    ans = []
    # 문자열을 i개 단위로 자르면서 확인할 것임
    for i in range(1,len(s)+1):
        # i개 단위로 잘랐을 때 변수를 점차 저장할 변수
        standard = ""
        # 직전 문자열
        start = s[:i]
        # 중복 되는 문자열 세는 변수
        cnt = 1

        # j는 i개만큼 문자열을 순차적으로 확인
        for j in range(i, len(s)+i, i):
            # i개 단위만큼 건너뛴 문자열과 직전 문자열이 같으면 cnt에 1 더함 
            if s[j:i+j] == start:
                cnt += 1
            else:
                # 직전 문자열이 2개 이상 중복된 수일 때
                if cnt > 1:
                    standard += str(cnt) + start
                else:
                    standard += start
                # 초기화
                cnt = 1
                start = s[j:i+j]  
        # i개 단위로 자른 문자열 = standard
        ans.append(len(standard))     
    return min(ans)
