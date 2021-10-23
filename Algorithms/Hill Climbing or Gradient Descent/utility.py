def hash_function(element_1, element_2):
    hash_value = 0
    for i in element_1:
        for j in element_2:
            if i == 0:
                i = 8
            if j == 0:
                j = 8
            hash_value += i ** j / i + j - i * j + i + j
    return hash_value
