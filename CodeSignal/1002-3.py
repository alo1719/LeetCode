from pydoc import doc


def solution(docstring: str):
    i = 0
    j = 0
    res = ''
    while (i < len(docstring)):
        if docstring[i] == '`':
            for j in range(i+1, len(docstring)):
                if docstring[j] == '`':
                    str = docstring[i:j+1]
                    print(str)
                    s2 = docstring[i+1:j]
                    print(s2)
                    a2 = s2.split(' ')
                    print(a2)
                    for k,ss in enumerate(a2):
                        if ss[0].isupper():
                            continue
                        temp = ''
                        ii = 0
                        while ii < len(ss):
                            if ss[ii] != '_':
                                temp+=(ss[ii])
                                ii+=1
                            else:
                                temp+=(ss[ii+1].upper())
                                ii+=2
                        print(temp)
                        a2[k] = temp
                    res += '`'
                    for jjj,ss in enumerate(a2):
                        res += ''.join(ss)
                        if jjj!=len(a2)-1: res += ' '
                    res += '`'
                    break
        else:
            res += docstring[i]
        i = max(j+1,i+1)

    return res

print(solution("123 `func_name C_NAME` 456 `max_x_y_z` `variable` `G`"))