# 통나무 자르기 (G1)
# L: 통나무길이
# K: 통나무 자를 수 있는 위치의 수
# C: 실제 자를 수 있는 최대 횟수

from sys import stdin

L, K, C = map(int, stdin.readline().split())

can_cut = list(set(map(int, stdin.readline().split())))
can_cut += [0, L]
can_cut.sort()

pieces = [can_cut[i] - can_cut[i-1] for i in range(len(can_cut)-1, 0, -1)]
longest = max(pieces)

def cut(length):
    if longest>length: return 10001, 0
    cnt = 0
    now_len = 0

    for piece in pieces:
        now_len += piece
        if now_len > length:
            now_len = piece
            cnt += 1

    return cnt, now_len if cnt == C else pieces[-1]

st, end = 0, L
shorted, ans_where = 0, 0
while st <= end:
    mid = (st+end)//2
    cnt, where = cut(mid)
    if cnt <= C:
        shorted = mid
        ans_where = where
        end = mid -1
    else:
        st = mid +1
    
print(shorted, ans_where)