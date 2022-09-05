# %% [markdown]
# # system of linear equations

# %% [markdown]
# a linear equation in variables x1,x2,..xn is an equation of the form a1x1, a2x2,...an,xn and $b$ are constants.
# 
# the constants ai is called the coefficient of xi

# %% [markdown]
# A system of linear equations is a finite collection of linear equations in the same variables.
# 
# linear wquations in $n$ variables $x_1, x_2. \ldots. x_n$ <br>
# 
# $a_{11}x_1 + a_{12}x_2 + \ldots + a_{1n}x_n = b_1$ <br>
# 
# $a_{21}x_1 + a_{22}x_2 + \ldots + a_{2n}x_n = b_2$ <br>
# 
# $\ldots$ <br>
# 
# $a_{m1}x_1 + a_{m2}x_2 + \ldots + a_{mn}x_n = b_m$ <br>

# %% [markdown]
#  A solution of a linear system is an assignment of values to the variables $x_1, x_2 \ldots, x_n$ such that each of the equations is satisfied. The set of all solutions of a linear system is called the solution set of the system

# %% [markdown]
# in a matrix notation a linear system is $AX = B$, where <br>
# 
# $A = \begin{bmatrix}
# a_{11} & a_{12} & \ldots & a_{1n} \\ 
# a_{11} & a_{12} & \ldots & a_{1n} \\ 
#     & \ldots & \\
# a_{m1} & a_{m2} & \ldots & a_{mn} \\ 
# \end{bmatrix} $ is the coefficient matrix , <br>
# 
# $X = \begin{bmatrix}
# x_1 \\
# x_2 \\
# \vdots \\
# x_n \\
# \end{bmatrix} $ and
# $B = \begin{bmatrix}
# xb1 \\
# b_2 \\
# \vdots \\
# b_n \\
# \end{bmatrix} $.
# 

# %% [markdown]
# python has numpy.linalg.solve() to solve these sytem of linear equations
# 
# syntax
# 
# numpy.linalg.solve(A,B)
# 

# %% [markdown]
# Q. Find all solutions for the linear system <br>
# 
# $x_1 + 2x_2 - x_3 = 1$ <br>
# $2x_1 + x_2 + 4x_3 = 2$ <br>
# $3x_1 + 3x_2 + 4x_3 = 1$
# 

# %%
import numpy as np
A = np.array([[1,2,-1],[2,1,4],[3,3,4]])
B = np.array([1,2,1])

print(np.linalg.solve(A,B))



# %%
A = np.matrix([[1,2,-1],[2,1,4],[3,3,4]])
B = np.matrix([1,2,1])

print(np.linalg.solve(A,B))

# %% [markdown]
# this is because $B$ is a $m \times 1$ matrix in the matrix equivalent of linear system of equations

# %%
A = np.matrix([[1,2,-1],[2,1,4],[3,3,4]])
B = np.matrix([[1],[2],[1]])

print(np.linalg.solve(A,B))

# %% [markdown]
#  The function np.linalg.solve() works only if A is a non-singular matrix

# %%
A = np.matrix([[1,-1,1,-1],[1,-1,1,1],[4,-4,4,0],[-2,2,-2,1]])
B = np.matrix([[2],[0],[4],[-3]])

print(np.linalg.solve(A,B))

# %% [markdown]
# this is because determinant of A is 0

# %% [markdown]
# linalg.solve() only works oif the matrix is a square matrix

# %%
A = np.matrix([[1,-1,1,-1],[1,-1,1,1],[4,-4,4,0]])
B = np.matrix([[2],[0],[4]])

print(np.linalg.solve(A,B))

# %%


# %% [markdown]
# ## Exercise problems

# %% [markdown]
# ### questions

# %% [markdown]
# 1.  write a program to solve any system of linear equations(user input), check whether the coefficient matrix is singular or not. If singular , print no solution. If non singular then print the inverse exst and solve the system of equation

# %%
l  = [int(x) for x in input("Enter coeefficirnts of  first equation : ").split()]
m  = [int(x) for x in input("Enter coeefficirnts of  second equation : ").split()]
n  = [int(x) for x in input("Enter coeefficirnts of  third equation : ").split()]

p  = [int(x) for x in input("Enter the three constants in order: ").split()]





import numpy as np
A = np.array([l,m,n])
B = np.array(p)
if  (A.shape[0] == A.shape[1]):
    de = np.linalg.det(A)
    if de ==0:
        print("determinant :\n", de)
        print("therefore no solution")
    else:
        print(np.linalg.solve(A,B))

        # using inverse method X = A^-1 * B

        x =np.linalg.inv(A).dot(B)
        print("uding inverse method = " ,x)
else:
    print("no solution- not square matrix")

# %% [markdown]
# 2. solve the following system of linear equations 
#     - $x_1 + 2x_2 - x_3 = -1$
#     - $2x_1 + x_2 + 4x_3 = 2$
#     - $3x_1 + 3x_2 + 4x_3 = 1$

# %%
import numpy as np
A = np.array([[1,2,-1],[2,1,4],[3,3,4]])
B = np.array([-1,2,1])
de = np.linalg.det(A)
if de ==0:

    print("determinant :\n", de)
    print("therefore no solution")
else:
    print(np.linalg.solve(A,B))

# %%
# using inverse method X = A^-1 * B

x =np.linalg.inv(A).dot(B)
x

# %% [markdown]
# 3. solve
#     - $x_1 - x_2 + x_3 - x_4 = 2$
#     - $x_1 - x_2 + x_3 + x_4 = 0$
#     - $4x_1 - 4x_2 + 4x_3 = 4$
#     - $-2x_1 + 2x_2 - 2x_3 + x_4 = -3$

# %%
A = np.matrix([[1,-1,1,-1],[1,-1,1,1],[4,-4,4,0],[-2,2,-2,1]])
B = np.matrix([[2],[0],[4],[-3]])
de = np.linalg.det(A)

if de ==0:

    print("determinant :\n", de)
    print("therefore no solution")
else:
    print(np.linalg.solve(A,B))

# %% [markdown]
# 4. solve
#     - $x_1 - 2x_2 - x_3 = 1$
#     - $2x_1 + x_2 - 5x_3 = 2$
#     - $3x_1 + 3x_2 + 4x_3 = 1$

# %%
import numpy as np
A = np.array([[1,-2,-1],[2,1,-5],[3,3,4]])
B = np.array([1,2,1])
de = np.linalg.det(A)
if de ==0:

    print("determinant :\n", de)
    print("therefore no solution")
else:
    print(np.linalg.solve(A,B))

# using inverse method X = A^-1 * B

x =np.linalg.inv(A).dot(B)
print("uding inverse method = " ,x)

# %% [markdown]
# 5. solve
#     - $x_1 + 2x_2 + x_3 = 4$
#     - $4x_1 + 5x_2 + 6x_3 = 7$
#     - $7x_1 + 8x_2 + 9x_3 = 10$

# %%
import numpy as np
A = np.array([[1,2,-1],[4,5,6],[7,8,9]])
B = np.array([4,7,10])
de = np.linalg.det(A)
if de ==0:

    print("determinant :\n", de)
    print("therefore no solution")
else:
    print(np.linalg.solve(A,B))

# using inverse method X = A^-1 * B

x =np.linalg.inv(A).dot(B)
print("uding inverse method = " ,x)

# %% [markdown]
# 5. solve
#     - $x_1 + 3x_2 - 5x_3 = 1$
#     - $4x_1 + 2x_2 + x_3 = 2$

# %%
import numpy as np
A = np.array([[1,3,-5],[4,2,1]])
B = np.array([1,2])
if  (A.shape[0] == A.shape[1]):
    de = np.linalg.det(A)
    if de ==0:
        print("determinant :\n", de)
        print("therefore no solution")
    else:
        print(np.linalg.solve(A,B))

        # using inverse method X = A^-1 * B

        x =np.linalg.inv(A).dot(B)
        print("uding inverse method = " ,x)
else:
    print("no solution- not square matrix")

# %% [markdown]
# 6. suppose a fruit seller sold 20 mangoes + 10 oranges in one day for 350 dollars. next day 17 mangoes + 22 oranges for 500 dollars. find the prices of one mango and one orange

# %%
import numpy as np
A = np.array([[20,10],[17,22]])
B = np.array([350,500])
de = np.linalg.det(A)
if de ==0:

    print("determinant :\n", de)
    print("therefore no solution")
else:
    print(np.linalg.solve(A,B))

# using inverse method X = A^-1 * B

x =np.linalg.inv(A).dot(B)
print("uding inverse method = " ,x)


