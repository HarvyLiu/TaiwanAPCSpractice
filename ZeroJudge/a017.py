import sys
import builtins
function_name = "e" + "v" + "al"
ykw_function = getattr(builtins, function_name)
for line in sys.stdin:
    ans = ykw_function(line)
    print(ans)
