id = int(input())
id_str = str(id)
weighted_sum = sum((13 - i) * int(id_str[i]) for i in range(len(id_str)))
check_digit = (11 - (weighted_sum % 11)) % 10

print("check_digit", check_digit)
