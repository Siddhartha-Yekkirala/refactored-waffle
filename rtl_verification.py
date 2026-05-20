def AND(a, b):
    return a & b

def XOR(a, b):
    return a ^ b

def verify_and():
    for a in [0,1]:
        for b in [0,1]:
            assert AND(a,b) == (a & b)

def verify_xor():
    for a in [0,1]:
        for b in [0,1]:
            assert XOR(a,b) == (a ^ b)

if __name__ == "__main__":
    verify_and()
    verify_xor()
    print("All RTL verification tests passed successfully")
