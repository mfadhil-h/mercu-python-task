def count_char(s=""):
    s = s.lower()
    char_dict = {}
    for c in s:
        if c in char_dict:
            char_dict[c] = char_dict[c] + 1
        else:
            char_dict[c] = 1
    return char_dict


total_char = count_char("aaabbbb")
print total_char
total_char = count_char("xyzsaab")
print total_char
total_char = count_char()
print total_char

