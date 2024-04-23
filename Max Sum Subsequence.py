def max_sum_subseq(list1):
    start_idx = 0
    end_idx = 0
    curr_sum = 0
    maxsum = -9999999999

    for j in range(0,len(list1)):
        curr_sum += list1[j]

        if curr_sum > maxsum:
            maxsum = curr_sum
            end_idx = j

        if curr_sum < 0:
            curr_sum = 0
            start_idx = j+1

    print("Max sum subsequence: ", list1[start_idx:end_idx+1])
    return maxsum
            

ques1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sum_subseq(ques1))
