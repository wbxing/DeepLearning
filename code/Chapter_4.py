import numpy as np

# 3*4的矩阵A
A = np.random.rand(3, 4)
print(A)

# A的转置
AT = A.T
print(AI)

# A 不可逆
# AI = np.linalg.inv(A) 

# A的伪逆
Ai = np.linalg.pinv(A)
print(Ai)

# 矩阵相乘
M1 = np.dot(A, Ai)
M2 = np.matmul(A, Ai)
print(M1, M2)

# 方阵As
As = np.random.rand(3, 3)
print(As)

# As的逆
Asi = np.linalg.inv(As)
print(Asi)

# 与逆矩阵相乘，由于误差的原因并不是标准单位阵
I1 = np.matmul(As, Asi)
I2 = np.dot(As, Asi)
print(I1, I2)

# 转为单位阵
Ii = np.random.rand(3, 3)
I = np.dot(As, Asi)
for i in range(3):
    for j in range(3):
        Ii[i][j] = int(I[i][j])
print(Ii)

B = np.random.randint(0, 10, (3, 3))
print(B)

Bi = np.linalg.inv(B)
print(Bi)

Ib = np.dot(B, Bi)
print(Ib)
