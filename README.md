# ACORN_V3
Simple encryption algorithm in Python

- This is a simple implementation of ACORN v3 in Python with minimal and simple encryption algorithm using XOR functions 
  operation.

- This Algorithm just encrypts a plaintext and using XOR operation with generated keystream, generates ciphertext without 
  authentication(without Associated Data)

- The file structure:

	* state.py = Define a State class with 293 bits and provides methods to get/set specific bits. 

	* feedback.py = Implement the feedback polynomial as defined in ACORN v3. Output the bit to be XORed into the state for                       update.

	* filter.py = generates the keystream in each iteration which further XORed with the plaintext to generate 
		            the ciphertext.

	* update.py = The state update function combines feedback and state shifting. Basically updates the internal state bits. 
                Should apply input bit (plaintext or associated data), control signals, and feedback output.

	* acorn.py = High-level class to handle:

			  Initialization with key and IV

			  Processing associated data

			  Encrypting plaintext (generating keystream and XORing)

			  Finalization(generating tag)

	* utils.py = Convert bytes to bits and back. XOR operations, hex conversion, etc.
	
	* test_vector.py = Load test vectors. Run encryption and compare outputs.

- To run test the encryption, open test_vector.py file, replace 'key', 'iv', 'plaintext' and 'expected_ciphertext_hex with 
  official test vector and run the file.

- If the output matches, "Test Passed" is printed else "Test Failed" is printed.

- The algorithm is not test with a official test vector. Instead, tested with a Chatgpt generated test vector (passed): 
		key = '000102030405060708090a0b',
		 IV = '0c0d0e0f1011121314151617',
		 plaintext = '0011223344556677',
		 expected_ciphertext_hex = 'a9fa6ece7bdef4dd'

