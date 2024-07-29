
import itertools
def merge_alternately(word1: str, word2: str) -> str:
    final_str = ""
    for w1, w2 in itertools.zip_longest(word1, word2):
        final_str += (w1 or "") + (w2 or "")
    return final_str
    # minLen = min(len(word1),len(word2))
    # merge = ""
    # for i in range(minLen):
    #     merge += word1[i] + word2[i]
    # merge += word1[minLen:] + word2[minLen:]
    # return merge


    # m = len(word1)
    # n = len(word2)
    # i = 0
    # j = 0
    # result = []
    #
    # while i < m or j < n:
    #     if i < m:
    #         result += word1[i]
    #         i += 1
    #     if j < n:
    #         result += word2[j]
    #         j += 1
    #
    # return "".join(result)

    #
    # result = []
    # n = max(len(word1), len(word2))
    # for i in range(n):
    #     if i < len(word1):
    #         result += word1[i]
    #     if i < len(word2):
    #         result += word2[i]
    #
    # return "".join(result)

final_str=merge_alternately("shaik", "john")
print(final_str)