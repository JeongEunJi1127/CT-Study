def solution(p):
    global answer
    answer = ""
    dfs(p)
    return answer

def dfs(p):
    global answer
    # 1. 입력이 빈 문자열이거나, p가 이미 "올바른 괄호 문자열"이라면 p를 그대로 반환합니다. 
    if len(p) == 0 or isright_p(p):
        answer += p
    else:
        # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" lp, rp로 분리합니다
        lp,rp = divide_balanced_p(p)
        # 3. 문자열 lp가 "올바른 괄호 문자열" 이라면 
        if isright_p(lp):
            answer += lp
            # 문자열 rp에 대해 1단계부터 다시 수행합니다. 
            dfs(rp)
        # 4. 문자열 lp가 "올바른 괄호 문자열"이 아니라면
        else:
            # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
            answer += "("
            #4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
            dfs(rp)  
            # 4-3. ')'를 다시 붙입니다. 
            answer += ")"
            # 4-4 lp의 첫 번째와 마지막 문자를 제거하고
            lp = lp[1:]
            lp = lp[:-1]
            # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
            new_lp = ""
            for i in lp:
                if i == "(":
                    new_lp += ")"
                elif i == ")":
                    new_lp += "("
            answer += new_lp
    return answer

# p가 올바른 문자열인지 확인하는 함수
def isright_p(p):
    lcnt = 0
    rcnt = 0
    for i in p:
        if rcnt > lcnt:
            return False
        if i == "(":
            lcnt += 1
        elif i == ")":
            rcnt += 1
    return True

# p를 균형잡힌 괄호 문자열 두개로 분리하는 함수
def divide_balanced_p(p):
    lcnt = 0
    rcnt = 0
    newp = ''

    for i in p:
        if lcnt == rcnt and lcnt != 0 and rcnt != 0:
            return (newp, p[len(newp):])
        if i == "(":
            lcnt += 1
        elif i == ")":
            rcnt += 1
        newp += i
    return (newp, p[len(newp):])

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
