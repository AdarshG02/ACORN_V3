# state.py

class ACORNState:
    def __init__(self):
        # Initialize 293-bit state to all zeros
        self.state = [0] * 293
    
    

    def get_bit(self, index: int) -> int:
        """Get the bit at position `index` in the state."""
        if 0 <= index < 293:
            return self.state[index]
        raise IndexError("State index out of bounds.")

    def set_bit(self, index: int, value: int):
        """Set the bit at position `index` in the state to 0 or 1."""
        if 0 <= index < 293:
            self.state[index] = value & 1  # Ensure it's only 0 or 1
        else:
            raise IndexError("State index out of bounds.")

    def shift_register(self, new_bit: int):
        """Shift the entire register left and insert new_bit at position 0."""
        #self.state = [new_bit & 1] + self.state[:-1]
        self.state = self.state[1:] + [new_bit]
        
    def load(self, bit_list: list):
        """Load a 293-bit list into the state."""
        if len(bit_list) != 293:
            raise ValueError("Input bit list must be 293 bits long.")
        self.state = bit_list.copy()

    def dump(self) -> list:
        """Return a copy of the current state."""
        return self.state.copy()

    