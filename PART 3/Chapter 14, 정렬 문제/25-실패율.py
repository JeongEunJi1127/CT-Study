def solution(N, stages):
    fail = []
    stages.sort()

    for i in range(1,N+1):
        k = stages.count(i)
        # 여기서 런타임 계속 걸림 -> 한줄로 처리
        fail_rate = k/len(stages) if len(stages) != 0 else 0
        fail.append((fail_rate,i))
        stages = stages[k:]

    fail.sort(key = lambda x:-x[0])
    fail = [x[1] for x in fail]
    return fail

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))