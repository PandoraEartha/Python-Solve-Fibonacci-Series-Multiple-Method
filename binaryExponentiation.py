import numpy


# 用快速幂算法求解斐波那契数列数列任意一项
# CALCULATE ANY TERM IN FIBONACCI SEQUENCE WITH BINARY EXPONENTIATION ALGORITHM
def fibonacci(n):
    if n<=0:
        print('n MUST BE GREATER THAN 0')
        return
    if n<=2:
        return 1
    A=numpy.array([[1,1],[1,0]],dtype=object)
    return numpy.linalg.matrix_power(A,n-2)[0][0]+numpy.linalg.matrix_power(A,n-2)[0][1]


# 用优化后的快速幂算法求解斐波那契数列数列任意一项
# CALCULATE ANY TERM IN FIBONACCI SEQUENCE WITH BINARY EXPONENTIATION ALGORITHM OPTIMIZED
# F(2n+1)=F^2(n+1)+F^2(n)
# F(2n)=F(n)*[F(n)+2*F(n-1)]
def fibonacciOptimize(n):
    if n<=0:
        print('n MUST BE GREATER THAN 0')
        return
    if n<=2:
        return 1
    A=numpy.array([[1,1],[1,0]],dtype=object)
    if n&1:
        A_power=numpy.linalg.matrix_power(A,(n>>1)-1)
        # F_N_Subtract1_divide2_Add1: F((n-1)/2+1)
        F_N_Subtract1_divide2_Add1=A_power[0][0]+A_power[0][1]
        # F_N_Subtract1_divide2: F((n-1)/2)
        F_N_Subtract1_divide2=A_power[1][0]+A_power[1][1]
        return (F_N_Subtract1_divide2_Add1*F_N_Subtract1_divide2_Add1)+(F_N_Subtract1_divide2*F_N_Subtract1_divide2)
    else:
        A_power=numpy.linalg.matrix_power(A,(n>>1)-2)
        # F_N_divide2: F(n/2)
        F_N_divide2=A_power[0][0]+A_power[0][1]
        # F_N_divide2_Subtract1: F(n/2-1)
        F_N_divide2_Subtract1=A_power[1][0]+A_power[1][1]
        return F_N_divide2*(F_N_divide2+(F_N_divide2_Subtract1<<1))
