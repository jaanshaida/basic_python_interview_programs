def reverse_of_sentence_words(input_str):
    str_list = input_str.split()
    return " ".join(str_list[::-1])


print(reverse_of_sentence_words("shaik john shaida"))
