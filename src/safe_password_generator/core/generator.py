"""
Core logic for secure password generation.
"""
import secrets
import string
from .exceptions import InvalidCriteriaError, MinimumLengthError

def generate_password(
    length: int = 16,
    use_upper: bool = True,
    use_lower: bool = True,
    use_numbers: bool = True,
    use_specials: bool = True,
) -> str:
    """
    Generates a secure random password based on the provided criteria.

    Args:
        length (int): Desired length of the password.
        use_upper (bool): Whether to include uppercase letters.
        use_lower (bool): Whether to include lowercase letters.
        use_numbers (bool): Whether to include numeric digits.
        use_specials (bool): Whether to include special characters.

    Returns:
        str: A securely generated random password.

    Raises:
        InvalidCriteriaError: If no character types are selected.
        MinimumLengthError: If the length is too short to satisfy the selected criteria.
    """
    if not any([use_upper, use_lower, use_numbers, use_specials]):
        raise InvalidCriteriaError("At least one character type must be selected.")

    character_pool = ""
    password_chars = []

    if use_upper:
        character_pool += string.ascii_uppercase
        password_chars.append(secrets.choice(string.ascii_uppercase))
    
    if use_lower:
        character_pool += string.ascii_lowercase
        password_chars.append(secrets.choice(string.ascii_lowercase))
        
    if use_numbers:
        character_pool += string.digits
        password_chars.append(secrets.choice(string.digits))
        
    if use_specials:
        # A curated list of readable and safe special characters
        specials = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        character_pool += specials
        password_chars.append(secrets.choice(specials))

    if length < len(password_chars):
        raise MinimumLengthError(
            f"Requested length {length} is too short. "
            f"Must be at least {len(password_chars)} to include all selected character types."
        )

    # Fill the remaining length required for the password
    remaining_length = length - len(password_chars)
    for _ in range(remaining_length):
        password_chars.append(secrets.choice(character_pool))

    # Shuffle the characters securely to prevent predictable patterns
    secrets.SystemRandom().shuffle(password_chars)
    
    return "".join(password_chars)
