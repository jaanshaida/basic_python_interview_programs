def reverse_each_word_of_sentence(input_str):
    return " ".join([word[::-1] for word in input_str.split()])


# print(reverse_each_word_of_sentence("shaik john shaida"))


# reverse every second 2nd position of the word in the sentence

def reverse_every_second_word_of_sentence(input_str):
    return " ".join([word[::-1] if (i % 2 != 0) else word for i, word in enumerate(input_str.split())])


print(reverse_every_second_word_of_sentence("shaik john shaida johnny joe joo"))
