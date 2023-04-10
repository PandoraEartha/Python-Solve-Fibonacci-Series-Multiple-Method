
# 用循环求解斐波那契数列任意一项
# CALCULATE ANY TERM IN FIBONACCI SEQUENCE USING LOOP
def fibonacci(n):
    if n<=0:
        print('n MUST BE GREATER THAN 0')
        return
    if n<=2:
        return 1
    FnSubtract1=1
    FnSubtract2=1
    Fn=0
    for i in range(2,n):
        Fn=FnSubtract1+FnSubtract2
        FnSubtract2=FnSubtract1
        FnSubtract1=Fn

    return Fn
