def score(x, y):
    OUTER_RADIUS = 10
    MIDDLE_RADIUS = 5
    INNER_RADIUS = 1
    score = 0

    pos = x**2 + y**2

    if(pos > OUTER_RADIUS**2):
        score = 0
    elif(pos > MIDDLE_RADIUS**2):
        score = 1
    elif(pos > INNER_RADIUS**2):
        score = 5
    else:
        score = 10

    return score
