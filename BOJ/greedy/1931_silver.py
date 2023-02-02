# N = int(input())
# timeList = []
# for _ in range(N):
#     timeList.append(list(map(int, input().split())))
# timeList.sort()

# removeList = []
# for i in range(N-1):
#     if timeList[i][0] == timeList[i+1][0] and timeList[i][0] != timeList[i][1]:
#         removeList.append(timeList[i+1])

# for i in range(len(removeList)):
#     timeList.remove(removeList[i])

# # print(timeList)

# maxCnt = 0
# while len(timeList) != 1:
#     newTimeList = timeList.copy()
#     cnt = 1
#     start = newTimeList[0][0]
#     end = newTimeList[0][1]
#     while len(newTimeList) != 1:
#         # print(newTimeList[0], end='')
#         newTimeList.pop(0)
#         if newTimeList[0][0] >= end:
#             end = newTimeList[0][1]
#             cnt += 1
#             # print(newTimeList[0], 'cnt=', cnt)
#     if maxCnt < cnt:
#         maxCnt = cnt
#     timeList.pop(0)


# print(maxCnt)

n = int(input())
s = []
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])
s = sorted(s, key=lambda a: a[0])
s = sorted(s, key=lambda a: a[1])
last = 0
cnt = 0
for i, j in s:
    if i >= last:
        cnt += 1
        last = j
print(cnt)
