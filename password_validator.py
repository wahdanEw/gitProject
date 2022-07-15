import re
from termcolor import colored
import sys


def validate_password(passwd) -> str:
    """
    an example: validate_password(my password) -> str(user message valid/invalid)
    :param passwd: str
    """
    if len(passwd) >= 10:
        if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{10,30})',passwd))==True):
            print(colored("your password is strong", "green"))
        else:
            print(colored("your password is weak", "red"))
    else:
        print(colored("You have entered an invalid password, "
                      "password should contain:\n"
                      "length minimum of 10 characters\n"
                      "alphabet and number, small and capital case letters", "red"))


def main():
    if len(sys.argv) == 3:
        if sys.argv[1] == "-f":
            path = sys.argv[2]
            with open(path, 'r') as f:
                contents = f.readline()
                validate_password(contents)
    elif len(sys.argv) == 2:
        validate_password(sys.argv[1])
    else:
        print(colored("Wrong input, an example for valid input:\n"
                      "python ./password_validator.py \"MyP@ssw0rd!\"\n"
                      "python ./password_validator.py \"/myPATH/password.txt\"", "red"))


if __name__ == '__main__':
    main()
