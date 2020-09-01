#leetcode 1021
def removeOuterParentheses(S: str) -> str:
    stack = ''
    flag = 0
    record = 0
    for i in range(len(S)):
        if S[i] == '(':
            if record == 0 and flag == 0:
                flag = 1
                pass
            else:
                stack = stack + '('
            record += 1
        else:
            if record == 1:
                flag = 0
                pass
            else:
                stack = stack + ')'
            record -= 1

    return stack

print(removeOuterParentheses("(()())(())"))