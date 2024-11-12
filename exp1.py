# Program to display the Fibonacci sequence up to n-th term using non-recursive
nterms = int(input("Enter number of terms "))
# first two terms
n1, n2 = 0, 1
count = 0
# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
    print("Fibonacci sequence upto", nterms,":")
    print(n1)
# generate fibonacci sequence
else:
    print("Fibonacci sequence using non-recursion:")
while count < nterms:
    print(n1)
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    count += 1


# Program to display the Fibonacci sequence up to n-th term using recursive method
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter number of terms:"))
print("Fibonacci sequence using recursion:")
for i in range(n):
    print(fibonacci(i))