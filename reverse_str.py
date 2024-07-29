# way 1
def reverse_str_by_slice_operator(input_str):
    return input_str[:: -1]


# way 2

def reverse_str_by_in_build_fun(input_str):
    return "".join(reversed(input_str))


def reverse_str_by_loop(input_str):
    rev_str = ''
    len_str = len(input_str)
    i = len_str - 1
    while i >= 0:
        rev_str += input_str[i]
        i -= 1
    return rev_str


print(reverse_str_by_loop("shaik"))

# print(reverse_str_by_in_build_fun("shaik"))
