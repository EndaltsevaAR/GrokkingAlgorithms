


def strings_to_table(str1, str2):
    table = [[]]
    table[0].append(0)
    for letter in str1:
        table[0].append(letter)
    for letter in str2:
        table.append([letter])
    return table

def find_max_substring(str1, str2):
    table = strings_to_table(str1, str2)
    max_len_substring = 0
    for y in range(1, len(table)):
        for x in range(1, len(table[0])):
            if y == x and table[y][0] == table[0][x]:
                new_cost = int(table[y-1][x-1]) + 1
                table[y].append(new_cost)
                if new_cost > max_len_substring:
                    max_len_substring = new_cost
            else:
                table[y].append(0)
    return max_len_substring


print(find_max_substring("hish", "fish"))
