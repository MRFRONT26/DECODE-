def binary_to_text(binary_str):
  """
  Decodes a binary string into its corresponding text or number.

  Args:
    binary_str: The binary string to decode.

  Returns:
    The decoded text or number.
  """

  try:
    # Attempt to decode as text
    text = ''.join(chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8))
    return text

  except ValueError:
    # If text decoding fails, try decoding as a number
    return int(binary_str, 2)

# Example usage
binary_string = "011001100110110001101111" 
decoded_value = binary_to_text(binary_string)
print(f"Decoded value: {decoded_value}")
