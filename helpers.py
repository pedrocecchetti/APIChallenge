import random, string

def randomString(stringLength):
    """
    Generate a random String with a combination of Lowercase
    and uppercase letters.
    The only parameter is the size of the String. 
    """

    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))
