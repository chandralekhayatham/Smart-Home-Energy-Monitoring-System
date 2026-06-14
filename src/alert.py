def get_status(power):

    if power >= 800:
        return "HIGH"

    elif power >= 400:
        return "NORMAL"

    else:
        return "LOW"