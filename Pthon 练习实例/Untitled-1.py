import sys
import pyperclip

PASSWORDS = {}

if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
else:
    print("This account is not in passwords.")
    