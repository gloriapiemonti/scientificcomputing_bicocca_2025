#From exercise Q11 - lesson 1

def winner(c1, c2, p1, p2):
    if c1 == "rock" and c2 == "scissors":
        p1 += 1
    elif c1 == "paper" and c2 == "rock":
        p1 += 1
    elif c1 == "scissors" and c2 == "paper":
        p1 += 1
    elif c1 == c2:
        pass
    else:
        p2 += 1

    return p1, p2