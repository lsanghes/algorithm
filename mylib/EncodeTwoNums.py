# k must be >= max(A,B)+1
def encode_two_nums(A, B, k):
    return A + B * k

# example
for A in [13, 20]:
    for B in [0, 1, 7, 30, 100]:
        k = max(A, B) + 1
        encoded = encode_two_nums(A, B, k)
        decode_A = encoded % k
        decode_B = encoded // k
        print((A, decode_A, B, decode_B, encoded))
