# filter.py

class FilterFunction:
    @staticmethod
    def compute(state_bits: list) -> int:
        """
        Implements the correct ACORN v3 filter function:

        z = s_12 ⊕ s_154 ⊕ (s_235 ∧ s_61) ⊕ (s_193 ∧ s_230)
            ⊕ (s_66 ∧ s_111) ⊕ (s_244 ∧ s_23) ⊕ (s_160 ∧ s_196 ∧ s_95)
        """
        s = state_bits

        if len(s) != 293:
            raise ValueError("State must be 293 bits.")

        z = (
            s[12] ^
            s[154] ^
            (s[235] & s[61]) ^
            (s[193] & s[230]) ^
            (s[66] & s[111]) ^
            (s[244] & s[23]) ^
            (s[160] & s[196] & s[95])
        )

        return z & 1
