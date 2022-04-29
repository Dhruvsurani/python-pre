
# 2. Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

def generate(result, s, open, close, n):
    if open == n and close == n:
        result.append(s)
        return
    if open < n:
        generate(result, s + "(", open + 1, close, n)
    if close < open:
        generate(result, s + ")", open, close + 1, n)

result = []
generate(result, "", 0, 0, 3)
print(result)