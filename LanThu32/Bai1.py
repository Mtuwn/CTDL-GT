# Tóm tắt bài 1: Tìm gcd(fib(a), fib(b)) % M

# Thuật toán:
# - gcd(fib(a), fib(b)) = fib(gcd(a,b))
# - Dùng chia để trị (ví dụ lũy thừa nhanh ma
# trận) để tính
# - Xử lí số (ví dụ dùng nhân ấn độ)

def matrix_mul(A, B, M):
    return [
        [
            (A[0][0]*B[0][0]  + A[0][1]*B[1][0]) % M,
            (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % M
        ],
        [
            (A[1][0]*B[0][0]  + A[1][1]*B[1][0]) % M,
            (A[1][0]*B[0][1]  + A[1][1]*B[1][1]) % M
        ]         
    ]

def matrix_pow(matrix, n, M):
    result = [[1,0],[0,1]]
    base = matrix
    while(n > 0): 
        if n %2 == 1:
            result = matrix_mul(result,base,M)
        base = matrix_mul(base, base, M)
        n //= 2
    return result


def fib(n, M):
    if n == 0:
        return 0
    
    F = [[1,1],[1,0]]
    result = matrix_pow(F, n, M)
    return result[0][1]

def gcd(a, b):
    while b:
        a,b = b, a%b
    return a

def gcd_fib_mob(a,b, M):
    gcd_ab = gcd(a,b)
    return fib(gcd_ab, M)

a = int(input('Nhap a: '))
b = int(input('Nhap b: '))
M = int(input('Nhap M: '))
print(gcd_fib_mob(a,b, M))