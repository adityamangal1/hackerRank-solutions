import re
s = input().strip()
k = input().strip()
s_len = len(s)
found_flag = False
for i in range(s_len):
    match_result = re.match(k, s[i:])
    print(match_result)
    if match_result:
        start_index = i + match_result.start()
        print(i)
        end_index = i+match_result.end()-1
        print((start_index, end_index))
        found_flag = True
if found_flag == False:
    print('(-1, -1)')
