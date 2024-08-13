""" Working With CLI — STDIN, STDOUT, STDERR """


# 1. Reading User Input
# Getting input from STDIN:

user_input = input("Impart your wisdom: ")
print(f"You shared: {user_input}")



# 2. Printing to STDOUT
# To print messages to the console:

print("Behold, the message of the ancients!")


# 3. Formatted Printing
# To weave variables into your messages with grace and precision:

name = "Merlin"
age = 300
print(f"{name}, of {age} years, speaks of forgotten lore.")


# 4. Reading Lines from STDIN
# Trim whitespaces line by line from STDIN:

import sys
for line in sys.stdin:
    print(f"Echo from the void: {line.strip()}")


# 5. Writing to STDERR
# To send message to STDERR:

import sys
sys.stderr.write("Beware! The path is fraught with peril.\n")


# 6. Redirecting STDOUT
# To redirect the STDOUT:

import sys
original_stdout = sys.stdout  # Preserve the original STDOUT
with open('mystic_log.txt', 'w') as f:
    sys.stdout = f  # Redirect STDOUT to a file
    print("This message is inscribed within the mystic_log.txt.")
sys.stdout = original_stdout  # Restore STDOUT to its original glory


# 7. Redirecting STDERR
# Redirecting STDERR:

import sys
with open('warnings.txt', 'w') as f:
    sys.stderr = f  # Redirect STDERR
    print("This warning is sealed within warnings.txt.", file=sys.stderr)


# 8. Prompting for Passwords
# To prompt for passwords:

import getpass
secret_spell = getpass.getpass("Whisper the secret spell: ")


# 9. Command Line Arguments
# Working with and parsing command line arguments:

import sys
# The script's name is the first argument, followed by those passed by the invoker
script, first_arg, second_arg = sys.argv
print(f"Invoked with the sacred tokens: {first_arg} and {second_arg}")


# 10. Using Argparse for Complex CLI Interactions
# Adding descriptions and options/arguments:

import argparse
parser = argparse.ArgumentParser(description="Invoke the ancient scripts.")
parser.add_argument('spell', help="The spell to cast")
parser.add_argument('--power', type=int, help="The power level of the spell")
args = parser.parse_args()
print(f"Casting {args.spell} with power {args.power}")






