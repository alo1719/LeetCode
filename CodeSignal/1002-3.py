# TC: O(n)  SC: O(n)
def solution(docstring: str):
    i = 0
    j = 0
    ans = ''
    while i < len(docstring):
        if docstring[i] == '`':
            for j in range(i+1, len(docstring)):
                if docstring[j] == '`':
                    str = docstring[i+1:j]
                    words = str.split(' ')
                    for k, each_word in enumerate(words):
                        if each_word[0].isupper(): continue
                        temp = ''
                        l = 0
                        while l < len(each_word):
                            if each_word[l] != '_':
                                temp += each_word[l]
                                l += 1
                            else:
                                temp += each_word[l+1].upper()
                                l += 2
                        words[k] = temp
                    ans += '`'+' '.join(words)+'`'
                    break
        else:
            ans += docstring[i]
        i = max(j+1, i+1)
    return ans

print(solution("123 `func_name C_NAME` 456 `max_x_y_z` `variable` `G`"))  # 123 `funcName C_NAME` 456 `maxXYZ` `variable` `G`
