

def solution(N):
    binary_str = bin(N)[2:]
    curr_gap = 0
    max_gap = 0
    for char in binary_str:
        if char == '0':
            curr_gap +=1
        else:
            max_gap = max(curr_gap, max_gap)
            curr_gap = 0
    return max_gap



def short_solution(N):
    binary = bin(N)[2:].strip("0").split("1")
    print(binary)
    return max(len(value) for value in binary)


print(short_solution(15))
print(solution(15))