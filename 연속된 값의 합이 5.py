# 사실 생각한 건 이건데
def linksum0(li, sumV):
    answer = 0
    for i in range(len(li)):
        if li[i] == 5:
            answer += 1
        else:
            for j in range(sumV):
                if sum(li[i:i+j]) == 5:
                    answer += 1
    return answer


# for 쓰지 말래서 손으로 for문 돌아갈 걸 작성함
def linksum1(li):
    answer = 0
    for i in range(len(li)):
        if li[i] == 5:
            answer += 1
        else:
            if i+2 <= len(li):
                if sum(li[i:i+2]) == 5:
                    answer += 1
            if i+3 <= len(li):
                if sum(li[i:i+3]) == 5:
                    answer += 1
            if i+4 <= len(li):
                if sum(li[i:i+4]) == 5:
                    answer += 1
            if i+5 <= len(li):
                if sum(li[i:i+5]) == 5:
                    answer += 1
    return answer


# 양심이 아파서 새로운 방법도 시도해 봄
def linksum2(li):
    answer, i, liSum = 0, 0, 0
    j = i
    while i <= len(li):
        if liSum <= 5 and j < len(li):
            liSum += li[j]
            if liSum == 5:
                answer += 1
            j += 1
        else:
            i += 1
            j = i
            liSum = 0
    return answer

print(linksum0([1, 2, 2, 3, 4, 1, 5], 5))
print("="*10)
print(linksum1([1, 2, 2, 3, 4, 1, 5]))
print("="*10)
print(linksum2([1, 2, 2, 3, 4, 1, 5]))