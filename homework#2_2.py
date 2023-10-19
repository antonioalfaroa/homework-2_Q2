def HamEncoding(x):
    m = len(x)
    k = 1
    while 2 ** k < m + k + 1:
        k += 1

    y = []
    j = 0

    for i in range(1, m + k + 1):
        if i == 2 ** j:
            y.append(0)
            j += 1
        else:
            y.append(int(x[i - j - 1]))

    for i in range(k):
        pos = 2 ** i
        count = 0
        for j in range(1, m + k + 1):
            if j & pos:
                count ^= y[j - 1]

        y[pos - 1] = count

    return ''.join(map(str, y))


def HamDecoding(rcv, k):
    Oldmsg = list(map(int, rcv))
    m = len(Oldmsg) - k
    error_pos = 0

    for i in range(k):
        pos = 2 ** i
        count = 0
        for j in range(1, m + k + 1):
            if j & pos:
                count ^= Oldmsg[j - 1]

        if count != 0:
            error_pos += pos

    if error_pos == 0:
        return 'No error'
    else:
        Oldmsg[error_pos - 1] ^= 1
        Newmsg = ''.join(map(str, Oldmsg))
        return f'Error at Position {error_pos}, and correct data: {Newmsg}'


org_sig1 = '1101'
encoded_sig1 = HamEncoding(org_sig1)
print(encoded_sig1)

org_sig2 = '1001011'
encoded_sig2 = HamEncoding(org_sig2)
print(encoded_sig2)

received_sig1 = '1010101'
k1 = 3
result1 = HamDecoding(received_sig1, k1)
print(result1)

received_sig2 = '1010001'
k2 = 3
result2 = HamDecoding(received_sig2, k2)
print(result2)

received_sig3 = '10110010011'
k3 = 4
result3 = HamDecoding(received_sig3, k3)
print(result3)

received_sig4 = '10110000011'
k4 = 4
result4 = HamDecoding(received_sig4, k4)
print(result4)
