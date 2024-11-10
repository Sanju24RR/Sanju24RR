# # Fibonacci Series (Recursive)
# n = int(input("Enter No : "))
# lst = [0,1]
# def fibo(s=0,i=1):
#     m = s + i
#     if n >= m:
#         lst.append(m)
#         s = i
#         i = m
#         fibo(s,i)
# fibo()
# print(lst)

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test the function
n_terms = 10
for i in range(n_terms):
    print(fibonacci_recursive(i), end=" ")
print()


# Fibonacci Series (Non-Recursive)
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Test the function
n_terms = 10
fibonacci_iterative(n_terms)
