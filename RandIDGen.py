import string, random
x = "".join(random.choice(string.digits+string.ascii_letters+string.punctuation) for i in range(15))
print(x)