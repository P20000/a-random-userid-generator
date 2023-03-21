def merge_strings(str1, str2):
    merged = ''
    for i, c in enumerate(str1):
        merged += c + str2[i % len(str2)]
    if len(str2) > len(str1):
        merged += str2[len(str1):]
    return merged


