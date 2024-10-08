def caesar_cipher(text, shift, encrypt=True):
  """Encrypts or decrypts a text using the Caesar cipher.

  Args:
    text: The text to be encrypted or decrypted.
    shift: The number of positions to shift the letters.
    encrypt: Whether to encrypt or decrypt the text (default: True).

  Returns:
    The encrypted or decrypted text.
  """

  result = ""
  for char in text:
    if char.isalpha():
      # Determine the starting index of the alphabet
      start = ord('a') if char.islower() else ord('A')

      # Calculate the shifted index, ensuring it stays within the alphabet
      shifted_index = (ord(char) - start + shift) % 26 + start

      # Convert the shifted index back to a character
      result += chr(shifted_index)
    else:
      # Keep non-alphabetic characters unchanged
      result += char

  return result

if __name__ == "__main__":
  text = input("Enter the text: ")
  shift = int(input("Enter the shift value: "))
  encrypt = input("Encrypt or decrypt? (e/d): ")

  if encrypt.lower() == 'e':
    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted text:", encrypted_text)
  elif encrypt.lower() == 'd':
    decrypted_text = caesar_cipher(text, -shift)
    print("Decrypted text:", decrypted_text)
  else:
    print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")