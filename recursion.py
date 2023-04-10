
# 递归求解斐波那契数列数列任意一项
# CALCULATE ANY TERM IN FIBONACCI SEQUENCE USING RECURSION
def fibonacci(n):
    if n<=0:
        print('n MUST BE GREATER THAN 0')
        return
    if n<=2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
