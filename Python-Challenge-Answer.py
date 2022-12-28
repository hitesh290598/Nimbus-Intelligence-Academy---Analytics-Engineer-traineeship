import random

def assignment():
    # stores a random integer A between 1 and 9
    A = random.randint(2, 8)
    # stores a random integer B between 1 and 9
    B= random.randint(2, 8)
    # multiplies A and B together as C
    C = A * B

    if C == 4:
        return print('Success! \n Values for A :', A, 'and B :', B)

    else:
        return print('Values for A :', A, 'and B :', B)

if __name__ == '__main__':
    assignment()