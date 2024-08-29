def addTwoNumbers(l1, l2):
    output = []
    bigger_list = l2 if len(l2) > len(l1) else l1
    smaller_list = l2 if len(l2) < len(l1) else l1
    remainder = 0
    for ind, val in enumerate(bigger_list):
        current_sum = l1[ind] + l2[ind] + remainder if ind < len(smaller_list) else l1[ind] + remainder
        string_sum = str(current_sum)

        if len(string_sum) == 2:
            output.append(eval(string_sum[0]) if ind == len(bigger_list) else eval(string_sum[-1]))
            remainder = eval(string_sum[0])

        else:
            output.append(current_sum)
            remainder = 0
    if remainder:
        output.append(remainder)
    print(output)

l1 = [2,4,3]
l2 = [5,6,4]

addTwoNumbers(l1, l2)

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

addTwoNumbers(l1, l2)