def validMoves(start, end):
    def helper(now, target):
        nonlocal global_ok
        ok = True
        for i in range(len(now)):
            if now[i] != target[i]:
                ok = False
                break
        if ok:
            global_ok = True
            return
        for i in range(len(now)):
            if now[i] == '_':
                continue
            if now[i] == 'R':
                if i+1 < n and now[i+1] == '_' and not global_ok:
                    now[i+1], now[i] = 'R',"_"
                    if str(now) not in v:
                        v.append(str(now))
                        helper(now, target)
                    now[i+1], now[i] = '_',"R"
                    if global_ok: rst.append(now.copy())
                if i+2 < n and now[i+2] == '_' and now[i+1] == 'B' and not global_ok:
                    now[i+2], now[i] = 'R',"_"
                    if str(now) not in v:
                        v.append(str(now))
                        helper(now, target)
                    now[i+2], now[i] = '_',"R"
                    if global_ok: rst.append(now.copy())
            if now[i] == 'B':
                if i-1 >= 0 and now[i-1] == '_' and not global_ok:
                    now[i-1], now[i] = 'B',"_"
                    if str(now) not in v:
                        v.append(str(now))
                        helper(now, target)
                    now[i-1], now[i] = '_',"B"
                    if global_ok: rst.append(now.copy())
                if i-2 >= 0 and now[i-2] == '_' and now[i-1] == 'R' and not global_ok:
                    now[i-2], now[i] = 'B',"_"
                    if str(now) not in v:
                        v.append(str(now))
                        helper(now, target)
                    now[i-2], now[i] = '_',"B"
                    if global_ok: rst.append(now.copy())
    v = []
    n = len(start)
    rst = []
    global_ok = False
    helper(start, end)
    if not rst:
        print(None)
    else:
        rst.reverse()
        rst.append(end)
        print(rst)

start_1 = ["R", "_", "B", "B"]
end_1 = ["B", "_", "B", "R"]
validMoves(start_1, end_1)