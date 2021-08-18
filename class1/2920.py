# 뭐가 틀린지 ㄹㅇ 모르겠다

sound = list(map(int, input().split()))
s = 0
i = 0
if sound[0] ==1:
    while sound[i+1] == sound[i] + 1:
        if i == len(sound)-2:
            s = 1
            print("ascending")
            break
        else:
            i = i + 1
i = 0
if sound[0] == 8:
    while sound[i + 1] == sound[i] -1:
        if i == len(sound) -2:
            s = 1
            print("descending")
            break
        else:
            i = i + 1
if s == 0:
    print("mixed")