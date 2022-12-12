def decimalToBinary(n):
    return bin(n).replace("0b", "")


def add(A, M):
    carry = 0
    add_sum = ''
    for i in range(len(A) - 1, -1, -1):
        temp = int(A[i]) + int(M[i]) + carry
        if (temp > 1):
            add_sum += str(temp % 2)
            carry = 1
        else:
            add_sum += str(temp)
            carry = 0
    return add_sum[::-1]


def compliment(m):
    M = ''
    for i in range(0, len(m)):
        M += str((int(m[i]) + 1) % 2)
    M = add(M, '0' * (len(M) - 1) + '1')
    return M


def restoringDivision(Q, M, A):
    count = len(M)
    print(f'Initial Values: A: {A}, Q: {Q}, M: {M}')
    while (count):
        print(f'Step: {len(M) - count + 1}', end=' ')
        print('Left Shift and Subtract: ', end=' ')
        A = A[1:] + Q[0]
        comp_M = compliment(M)
        A = add(A, comp_M)
        print(f'A: {A}')
        print(f'A: {A}, Q: {Q[1:]}_', end='')
        if (A[0] == '1'):
            Q = Q[1:] + '0'
            print('  -Unsuccessful')
            A = add(A, M)
            print(f'A: {A}, Q: {Q}  -Restoration')
        else:
            Q = Q[1:] + '1'
            print('  -Successful')
            print(f'A: {A}, Q: {Q}  -No Restoration')
        count -= 1
    print()
    print(f'Quotient(Q): {Q}, Remainder(A): {A}')


if __name__ == "__main__":
    tdividend = int(input('Enter dividend: '))
    dividend = decimalToBinary(tdividend)
    tdivisor = int(input('Enter divisor: '))
    divisor = '0'+decimalToBinary(tdivisor)
    print(divisor)
    accumulator = '0' * len(dividend)
    restoringDivision(dividend, divisor, accumulator)
