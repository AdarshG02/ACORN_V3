# feedback.py

class FeedbackFunction:
    @staticmethod
    def compute(state_bits: list, ca: int, cb: int, input_bit: int) -> int:
        """
        Implements the correct feedback function from ACORN v3:
        
        f = s_0 ⊕ (s_107 ∧ s_244) ⊕ s_23 ⊕ (ca ∧ s_196) ⊕ (cb ∧ input_bit)
        """
        s = state_bits

        if len(s) != 293:
            raise ValueError("State must be 293 bits.")

        f = (
            s[0] ^
            (s[107] & s[244]) ^
            s[23] ^
            (ca & s[196]) ^
            (cb & input_bit)
        )

        return f & 1  # Ensure result is a single bit
