answer = ""

num = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
button = {1:0,2:0,3:1,4:0,5:0,
          6:0,7:0,8:0,9:0}

for i in button:
    print("button의 i값입니다.",i)
    if button[i] == 1:
        print("ㅇㅇㅇㅇㅇㅇ",i)


print(button[3])
# for i in num: 뭐ㅓ라고?
#     a = 0
#     if button[i] == 1:

#     if i == 1 or i == 4 or i == 7:
#         button[i] = 1
#         answer += "L"
#     elif i == 3 or i == 6 or i == 9:
#         button[i] = 2
#         answer += "R"
#     elif (i -  
