
class Anagram:
    def __init__(self, A, k):
        freq_tables = []
        my_freq_table = [0] * 26

        for i in range(k):
            index = ord(A[i]) - 97
            my_freq_table[index] += 1

        freq_tables.append(my_freq_table)

        for i in range(1, len(A) - k + 1):
            my_freq_table = freq_tables[i - 1].copy()

            sub_index = ord(A[i - 1]) - 97
            my_freq_table[sub_index] -= 1

            add_index = ord(A[i + k - 1]) - 97
            my_freq_table[add_index] += 1

            freq_tables.append(my_freq_table)

        self.hashmap = dict()
        for i in range(len(freq_tables)):
            freq_tables[i] = tuple(freq_tables[i])
            if freq := self.hashmap.get(freq_tables[i]):
                self.hashmap.update({freq_tables[i]: freq + 1})

            else:
                self.hashmap.update({freq_tables[i]: 1})

    def anagram_count(self, B):
        freq_table = [0] * 26
        for i in range(len(B)):
            index = ord(B[i]) - 97
            freq_table[index] += 1

        if freq := self.hashmap.get(tuple(freq_table)):
            return freq

        return 0


def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    A = []
    ##################
    # YOUR CODE HERE #
    ##################
    anagram = Anagram(T, len(S[0]))
    for word in S:
        A.append(anagram.anagram_count(word))

    return tuple(A)
