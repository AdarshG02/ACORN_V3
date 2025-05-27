# acorn.py

from state import ACORNState
from update import update_state, generate_keystream_bit
from utils import bytes_to_bits, bits_to_bytes

class ACORNv3:
    def __init__(self, key: bytes, iv: bytes):
        if len(key) != 12 or len(iv) != 12:
            raise ValueError("Key and IV must be 93 bits (12 bytes) each.")

        self.key = key
        self.iv = iv
        self.state = ACORNState()

    def initialize(self):
        """
        Initialization phase:
        Load key and IV bits into the state as per ACORN spec,
        then run the initialization rounds.
        """
        # Load key + IV bits and initialize state bits
        k_bits = bytes_to_bits(self.key)[:93]
        iv_bits = bytes_to_bits(self.iv)[:93]

        # Construct initial state bits (293 bits) as per spec:
        # First 93 bits key, next 93 bits IV, then 293-93-93 = 107 zeros
        initial_bits = k_bits + iv_bits + [0]*107
        self.state.load(initial_bits)

        # Run initialization rounds (e.g. 1792 steps with control bits)
        for i in range(1792):
            # For now, we simplify control bits and input bit to 0; 
            # full spec handles CA, CB and input bits carefully.
            if i < 93:
                input_bit = k_bits[i]

            elif i < 186:
                input_bit = iv_bits[i - 93]
            
            else:
                input_bit=0

            self.state.load(update_state(self.state.dump(), ca=1, cb=1, input_bit = input_bit))

    def encrypt(self, plaintext: bytes) -> bytes:
        """
        Encrypt the plaintext using ACORN v3.
        For simplicity, associated data and finalization are skipped here.
        """
        pt_bits = bytes_to_bits(plaintext)
        ct_bits = []

        for bit in pt_bits:
            ks_bit = generate_keystream_bit(self.state.dump())
            ct_bit = ks_bit ^ bit

            ct_bits.append(ct_bit)

            # Update state with plaintext bit and control bits (simplified)
            self.state.load(update_state(self.state.dump(), ca=0, cb=0, input_bit=bit))
            print("Keystream Bit:", ks_bit, "Plaintext Bit:", bit, "Cipher Bit:", ct_bit)


        return bits_to_bytes(ct_bits)
