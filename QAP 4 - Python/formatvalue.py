# Format Values

# Uppercases first letter of inputs

def to_upper_title(letter):
    return letter.title()

# Uppercases the whole word

def to_upper_case(word):
    return word.upper()

# Formats money to two decimal places, adds commas and adds the dollar sign

def format_dollar(dollar):
    return "${:,.2f}".format(dollar)