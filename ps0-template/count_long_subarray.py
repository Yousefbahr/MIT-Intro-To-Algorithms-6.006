def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    ##################
    # YOUR CODE HERE #
    ##################
    current_subarray = 1
    longest_subarray = 1
    for x, y in zip(A, A[1:]):
        if y > x:
            current_subarray += 1
        # if comparing last two elements or y <= x
        if y <= x or A[-1] == y:
            # if current subarray is longer than the longest subarray
            # update the longest subarray and reset count
            if current_subarray > longest_subarray:
                longest_subarray = current_subarray
                count = 0
            # if current subarray is of same length as longest subarray , increment count
            if current_subarray == longest_subarray:
                count += 1
            # reset length of current subarray if there is a smaller value
            current_subarray = 1

    # Longest increasing subarray is of size 1
    # So return 0
    if longest_subarray == 1:
        return 0

    return count
