import re
User = input()
final_list = re.findall(
    r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([aeiouAEIOU]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', User)
if final_list:
    for i in final_list:
        print(i)
    else:
        print(-1)
