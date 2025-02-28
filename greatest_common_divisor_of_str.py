
def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 == str2: return str1

    if len(str2) > len(str1): str1, str2 = str2, str1

    if str1[:len(str2)] != str2: return ""

    return gcdOfStrings(str1[len(str2):], str2)

    # if str1 + str2 != str2 + str1:
    #     return ""
    #
    # from math import gcd
    # print(gcd(len(str1), len(str2)))
    # return str1[:gcd(len(str1), len(str2))]

    