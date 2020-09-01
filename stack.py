#leetcode 1021
def removeOuterParentheses(S: str) -> str:
    stack = ''
    record = 0
    for i in range(len(S)):
        if S[i] == '(':
            if record != 0 :
                stack = stack + '('
            record += 1
        else:
            if record != 1:
                stack = stack + ')'

            record -= 1

    return stack
print(removeOuterParentheses('(()())()()'))



def runningSum(nums):
    result = []
    if len(nums) >= 1:
        result.append(nums[0])
    else:
        return -1
    for i in range(1, len(nums)):
        result[i] = result[i - 1] + nums[i]
    return result
# print(runningSum([1,2,3,4]))