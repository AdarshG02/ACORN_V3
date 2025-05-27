# test_vector.py

from acorn import ACORNv3

def run_test_vector():
    # Sample test vector from ACORN v3 spec (replace with official vector)
    key = bytes.fromhex('000102030405060708090a0b')
    iv = bytes.fromhex('0c0d0e0f1011121314151617')
    plaintext = bytes.fromhex('0011223344556677')  
    
    expected_ciphertext_hex = 'a9fa6ece7bdef4dd'  # Replace with official ciphertext

    cipher = ACORNv3(key, iv)
    cipher.initialize()
    ciphertext = cipher.encrypt(plaintext)

    print("Ciphertext:", ciphertext.hex())
    print("Expected :", expected_ciphertext_hex)

    if ciphertext.hex() == expected_ciphertext_hex.lower():
        print("Test Passed!")
    else:
        print("Test Failed!")

if __name__ == "__main__":
    run_test_vector()
