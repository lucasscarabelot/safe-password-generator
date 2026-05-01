"""
Custom exceptions for the Safe Password Generator core module.
"""

class PasswordGeneratorError(Exception):
    """Base exception for all password generator errors."""
    pass

class InvalidCriteriaError(PasswordGeneratorError):
    """Raised when the provided criteria for password generation are invalid."""
    pass

class MinimumLengthError(PasswordGeneratorError):
    """Raised when the requested password length is smaller than the required criteria."""
    pass
