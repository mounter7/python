def print_multiplication_table(n):
    for i in range (1, 11):
        for j in range (1, n+1):
            print (i * j, end='\t')
        print()

if __name__ == '__main__':
    mul = int(input("n: "))
    print_multiplication_table(mul)