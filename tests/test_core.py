import string
import pytest
from safe_password_generator.core.generator import generate_password
from safe_password_generator.core.exceptions import InvalidCriteriaError, MinimumLengthError

def test_generate_password_length():
    """Test that the generated password has the exact requested length."""
    pwd = generate_password(length=20)
    assert len(pwd) == 20

def test_generate_password_contains_upper():
    """Test that the password contains at least one uppercase letter if requested."""
    pwd = generate_password(length=10, use_upper=True, use_lower=False, use_numbers=False, use_specials=False)
    assert any(c in string.ascii_uppercase for c in pwd)
    # Since only uppercase is requested, all characters should be uppercase
    assert all(c in string.ascii_uppercase for c in pwd)

def test_generate_password_contains_all_criteria():
    """Test that the password contains at least one character from each requested pool."""
    pwd = generate_password(length=12, use_upper=True, use_lower=True, use_numbers=True, use_specials=True)
    assert any(c in string.ascii_uppercase for c in pwd)
    assert any(c in string.ascii_lowercase for c in pwd)
    assert any(c in string.digits for c in pwd)
    
    specials = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    assert any(c in specials for c in pwd)

def test_generate_password_no_criteria_raises_error():
    """Test that requesting a password with no character types raises an InvalidCriteriaError."""
    with pytest.raises(InvalidCriteriaError):
        generate_password(use_upper=False, use_lower=False, use_numbers=False, use_specials=False)

def test_generate_password_length_too_short_raises_error():
    """Test that requesting a length smaller than the number of active criteria raises a MinimumLengthError."""
    with pytest.raises(MinimumLengthError):
        # 4 criteria are True by default, length 3 is too short
        generate_password(length=3)

def test_generate_password_length_matches_criteria():
    """Test edge case where length exactly matches the number of criteria."""
    pwd = generate_password(length=4)
    assert len(pwd) == 4
    
    # Must contain exactly one of each
    assert sum(1 for c in pwd if c in string.ascii_uppercase) == 1
    assert sum(1 for c in pwd if c in string.ascii_lowercase) == 1
    assert sum(1 for c in pwd if c in string.digits) == 1
    
    specials = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    assert sum(1 for c in pwd if c in specials) == 1
