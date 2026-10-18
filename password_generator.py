import secrets
import string

PASSWORD_LENGTH = 15
CHARACTER_GROUPS = (
    string.ascii_lowercase,
    string.ascii_uppercase.replace("O", ""),
    string.digits.replace("0", ""),
    string.punctuation,
)
CHARACTERS = "".join(CHARACTER_GROUPS)

def generate_password() -> str:
    first_letter_group = secrets.choice(CHARACTER_GROUPS[:2])
    other_letter_group = (
        CHARACTER_GROUPS[1]
        if first_letter_group == CHARACTER_GROUPS[0]
        else CHARACTER_GROUPS[0]
    )
    password = [
        secrets.choice(first_letter_group),
        secrets.choice(other_letter_group),
        secrets.choice(CHARACTER_GROUPS[2]),
        secrets.choice(CHARACTER_GROUPS[3]),
    ]
    remaining_characters = [
        secrets.choice(CHARACTERS)
        for _ in range(PASSWORD_LENGTH - len(password))
    ]
    secrets.SystemRandom().shuffle(remaining_characters)
    password.extend(remaining_characters)
    return "".join(password)


if __name__ == "__main__":
    print(generate_password())
