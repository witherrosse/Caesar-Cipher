import string

ALPHABET_LOWER = string.ascii_lowercase
ALPHABET_UPPER = string.ascii_uppercase


def caesar_cipher(text: str, shift: int, mode: str = "encode") -> str:
    """
    Encode or decode a text using Caesar Cipher.

    Args:
        text (str): Input text
        shift (int): Number of letters to shift
        mode (str): "encode" or "decode"

    Returns:
        str: Ciphered text
    """
    if mode == "decode":
        shift = -shift

    result = []

    for char in text:
        if char.islower():
            index = (ALPHABET_LOWER.index(char) + shift) % 26
            result.append(ALPHABET_LOWER[index])
        elif char.isupper():
            index = (ALPHABET_UPPER.index(char) + shift) % 26
            result.append(ALPHABET_UPPER[index])
        else:
            result.append(char)  # Non-alphabetic characters unchanged

    return "".join(result)


def main():
    print("🔐 Welcome to Caesar Cipher!")
    mode = input("Type 'encode' to encrypt, 'decode' to decrypt: ").strip().lower()
    text = input("Enter your message: ")
    shift = int(input("Enter shift number: "))

    ciphered_text = caesar_cipher(text, shift, mode)
    print(f"\nResult: {ciphered_text}")


if __name__ == "__main__":
    main()
