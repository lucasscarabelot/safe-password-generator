import argparse
import sys
from safe_password_generator.core.generator import generate_password
from safe_password_generator.core.exceptions import PasswordGeneratorError

def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Safe Password Generator CLI - Create secure, random passwords."
    )
    
    parser.add_argument(
        "-l", "--length",
        type=int,
        default=16,
        help="Length of the generated password (default: 16)"
    )
    parser.add_argument(
        "--no-upper",
        action="store_true",
        help="Exclude uppercase letters"
    )
    parser.add_argument(
        "--no-lower",
        action="store_true",
        help="Exclude lowercase letters"
    )
    parser.add_argument(
        "--no-numbers",
        action="store_true",
        help="Exclude numeric digits"
    )
    parser.add_argument(
        "--no-specials",
        action="store_true",
        help="Exclude special characters"
    )

    args = parser.parse_args()

    use_upper = not args.no_upper
    use_lower = not args.no_lower
    use_numbers = not args.no_numbers
    use_specials = not args.no_specials

    try:
        password = generate_password(
            length=args.length,
            use_upper=use_upper,
            use_lower=use_lower,
            use_numbers=use_numbers,
            use_specials=use_specials
        )
        # Using print directly for the CLI tool to allow piping to other tools
        print(password)
    except PasswordGeneratorError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
