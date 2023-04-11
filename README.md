# Python-Solve-Fibonacci-Series-Multiple-Method
Use Python to solve any term of Fibonacci Series with multiple method

利用Python求斐波那契数列任意一项的多种方法

[简体中文介绍](https://zhuanlan.zhihu.com/p/620719695)

#Usage

Download and extract the Source Code in Releases, that is all the code needed.

Change the code in main.py, for example, if you want to use recursion method, please use 

```recursion.fibonacci(n)```

if you want to use the optimized Binary Exponentiation method, please use 

```binaryExponentiation.fibonacciOptimize(n)```

but before use these method, you must import these Python source file.

```python
import recursion
import loop
import binaryExponentiation
```

And note that Binary Exponentiation method reauire numpy package.

#Algorithm

Recursion, Loop, Binary Exponentiation and optimized.


Recursion / Loop:

$F(n)=F(n-1)+F(n-2)$

Binary Exponentiation:

$\left[ \begin{matrix} F(n)\\F(n-1) \end{matrix} \right]=\left[ \begin{matrix} 1&&1\\1&&0 \end{matrix} \right]^{n-2}\left[ \begin{matrix} 1\\1 \end{matrix} \right]=A^{n-2}\left[ \begin{matrix} 1\\1 \end{matrix} \right]$

Binary Exponentiation optimized:

$F(2n+1)=F^2(n+1)+F^2(n)\\$

$F(2n)=F(n)\big[F(n+1)+F(n-1)\big]$

$\left[ \begin{matrix} F(n)\\F(n-1) \end{matrix} \right]=\left[ \begin{matrix} 1&&1\\1&&0 \end{matrix} \right]^{n-2}\left[ \begin{matrix} 1\\1 \end{matrix} \right]=A^{n-2}\left[ \begin{matrix} 1\\1 \end{matrix} \right]$
***

[算法详解(简体中文)](https://zhuanlan.zhihu.com/p/620719695)
