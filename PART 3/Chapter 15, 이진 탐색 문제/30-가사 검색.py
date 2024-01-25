from bisect import bisect_left, bisect_right

# list에서 start부터 end까지의 원소의 개수 구하는 함수
# ex) 'frame', -> 'frodo', 'front', 'frost' <-, 'kakao'
def count_range(l,start,end):
    return bisect_right(l,end) - bisect_left(l,start)

def solution(words, queries):
    answer = []
    # 단어의 길이는 최대 10000
    d = [[] for _ in range(10001)]
    # 뒤집은 d 배열
    reversed_d = [[] for _ in range(10001)]

    for word in words:
        d[len(word)].append(word)
        reversed_d[len(word)].append(word[::-1])
    
    for i in range(10001):
        d[i].sort()
        reversed_d[i].sort()
    
    for query in queries:
        # 키워드가 알파벳으로 시작하면
        if query[0] != "?":
            # 길이가 len(query)인 단어들에 대해, froaa ~ frozz에 속하는 단어의 개수 구함
            ans = count_range(d[len(query)], query.replace("?", "a"), query.replace("?","z"))
        # 키워드가 알파벳으로 시작하면 뒤집어서 알파벳으로 시작하게 하고
        else:
            # 길이가 len(query)인 뒤집힌 단어들에 대해, aaaao ~ zzzzo에 속하는 단어의 개수 구함
            ans =  count_range(reversed_d[len(query)], query[::-1].replace("?", "a"), query[::-1].replace("?","z"))
        answer.append(ans)
    return answer
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))