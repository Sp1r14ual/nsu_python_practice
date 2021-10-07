def hare(n, calls, recursion_count):
    if calls == 1:
        print("(\___/)", end="")
        if recursion_count < n - 1:
            print(" ", end="")
            hare(n, calls, recursion_count + 1)
        else:
            print()
            return
        
    if calls == 2:
        print("(='.'=)", end="")
        if recursion_count < n - 1:
            print(" ", end="")
            hare(n, calls, recursion_count + 1)
        else:
            print()
            return
        
    if calls == 3:
        print('(")_(")', end="")
        if recursion_count < n - 1:
            print(" ", end="")
            hare(n, calls, recursion_count + 1)
        else:
            print()
            return
        


function_call_number = 0
n = int(input())

function_call_number += 1
hare(n, function_call_number, 0)

function_call_number += 1
hare(n, function_call_number, 0)

function_call_number += 1
hare(n, function_call_number, 0)

#А что не так? Вы сами мне запретили использовать циклы