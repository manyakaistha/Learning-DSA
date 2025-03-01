def reverse_str(s):
    if not s:
        return ''
    return reverse_str(s[1:]) + s[0]

print(reverse_str("manya"))
