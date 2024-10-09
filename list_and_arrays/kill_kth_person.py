def find_survive_pos(n, k):
    n_list = list(range(n))
    n_list = n_list[k+1:] + n_list[:k]

    while len(n_list) > 1:
        n_list = n_list[k:] + n_list[:k -1]
        print(n_list)

        if 1 < len(n_list) < k:
            n_list.pop(len(n_list) // k)
            break
    print(n_list[0])

# input 1
n = 7
k = 3

# input 2
n = 5
k = 2


find_survive_pos(n, k)
# [0, 1, 2, 3, 4, 5, 6]
# # 3 killed
# [4, 5, 6, 0, 1, 2]
# # 6 killed
# [0, 1, 2, 4, 5]
# # 2 killed
# [4, 5, 0, 1]
# # 0 killed
# [1, 4, 5]
# # 5 killed
#
# [1, 4]
# if len(list) < k:
#     n_list.pop(len(n)//2)