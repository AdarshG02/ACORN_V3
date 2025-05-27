# utils.py

def bytes_to_bits(data: bytes) -> list:
    """
    Convert bytes to a list of bits (0 or 1).
    MSB first in each byte.
    """
    bits = []
    for byte in data:
        for i in range(7, -1, -1):  # from MSB to LSB
            bits.append((byte >> i) & 1)
    return bits

def bits_to_bytes(bits: list) -> bytes:
    """
    Convert a list of bits (0 or 1) to bytes.
    Assumes bits length is a multiple of 8.
    MSB first in each byte.
    """
    if len(bits) % 8 != 0:
        raise ValueError("Bits length must be multiple of 8.")

    bytes_out = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for j in range(8):
            byte = (byte << 1) | bits[i + j]
        bytes_out.append(byte)
    return bytes(bytes_out)
