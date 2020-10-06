user_lst = input().split()
i = 0

for i in range(2, len(user_lst)-1, 2):
    user_lst[i], user_lst[i+1] = user_lst[i+1], user_lst[i]

print(user_lst)
