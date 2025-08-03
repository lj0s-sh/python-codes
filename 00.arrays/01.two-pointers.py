def invert_full_string(s):
    chars = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return ''.join(chars)

# To fix
def invert_each_word(s):
    chars = list(s)
    left, right, aux = 0, 0, 0
    res = ''

    while right < len(chars):
        if chars[right] != ' ':
            right += 1
        else:
            res += ''.join(chars[left:right][::-1])
            right += 1
            left = right

    print(res)

print(invert_full_string('foo'))