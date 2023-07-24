def nonrec():
    f0 = 0
    f1 = 1
    for i in range(1, n - 1):
        fib = f0 + f1
        f0 = f1
        f1 = fib
        print(fib," ")
    if n > 1:  
        fib = f0 + f1
        print(fib)

def rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec(n - 1) + rec(n - 2)
    
def menu():
    print("\n Menu")
    print("1.Non recursive approach ")
    print("2.Recursive approach ")
    print("3.Exit ")    



while True:
    menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Enter the number upto which fibonacci series should be generated: ")
        n=int(input())
        nonrec()
    elif choice == 2:
        print("Enter the number upto which fibonacci series should be generated: ")
        n=int(input())
        for i in range(n):
            print(rec(i), end=" ")

    elif choice == 3:
        break

    else:
        print("Invalid choice. Please try again.")

