import random
import string
str = list(string.ascii_lowercase) * 10
str_list = list(str)
random.shuffle(str_list)
shuffled_str = ''.join(str_list)

index = 0
row_length = 1

while row_length <= 22:
    print(shuffled_str[index:index + row_length])
    index += row_length
    row_length += 1
    
    