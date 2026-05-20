import random
import logging

logging.basicConfig(filename="verification_log.txt", level=logging.INFO)

# ---------------- LOGIC CIRCUITS ---------------- #

def AND(a, b):
    return a & b

def XOR(a, b):
    return a ^ b

def ADDER_1BIT(a, b, cin):
    sum_ = a ^ b ^ cin
    carry = (a & b) | (b & cin) | (a & cin)
    return sum_, carry

# ---------------- TEST VECTOR GENERATOR ---------------- #

def generate_vectors(n=10):
    vectors = []
    for _ in range(n):
        a = random.randint(0, 1)
        b = random.randint(0, 1)
        cin = random.randint(0, 1)
        vectors.append((a, b, cin))
    return vectors

# ---------------- VERIFICATION ENGINE ---------------- #

def verify_adder():
    print("Running Adder Verification...")
    
    for a, b, cin in generate_vectors():
        expected_sum = (a ^ b ^ cin)
        expected_carry = (a & b) | (b & cin) | (a & cin)

        actual_sum, actual_carry = ADDER_1BIT(a, b, cin)

        assert actual_sum == expected_sum, f"SUM mismatch {a,b,cin}"
        assert actual_carry == expected_carry, f"CARRY mismatch {a,b,cin}"

        logging.info(f"PASS: {a},{b},{cin}")

    print("Adder Verification PASSED")

# ---------------- RUN ---------------- #

if __name__ == "__main__":
    verify_adder()
