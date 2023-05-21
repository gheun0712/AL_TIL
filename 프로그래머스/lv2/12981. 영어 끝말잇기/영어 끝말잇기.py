def solution(n, words):

    for i in range(1, len(words)):
        # 앞글자 끝말잇기를 하지 않았거나 앞서 말한 단어 얘기했을 시 게임 종료
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            return (i % n + 1, i // n + 1)
    else:
        return [0, 0]