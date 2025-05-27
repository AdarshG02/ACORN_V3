# update.py

from feedback import FeedbackFunction
from filter import FilterFunction

def update_state(state_bits: list, ca: int, cb: int, input_bit: int) -> list:
    """
    Update the ACORN v3 state by one step.

    Steps:
    1. Compute feedback bit using FeedbackFunction.
    2. Shift the state left by 1 bit.
    3. Insert the feedback bit at position 0.
    
    Args:
      state_bits: current 293-bit list representing the state
      ca, cb: control bits (phase dependent)
      input_bit: plaintext or associated data bit

    Returns:
      new_state_bits: updated 293-bit state after one iteration
    """
    # Compute feedback bit
    feedback_bit = FeedbackFunction.compute(state_bits, ca, cb, input_bit)
    
    # Shift and insert feedback bit at front
    new_state = [feedback_bit] + state_bits[:-1]
    
    return new_state


def generate_keystream_bit(state_bits: list) -> int:
    """
    Extract a keystream bit using the filter function.
    """
    return FilterFunction.compute(state_bits)
