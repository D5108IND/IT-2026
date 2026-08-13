def logistic_level(available):

    if available >= 0.9:
        return "Висока"
    elif available >= 0.6:
        return "Середня"
    else:
        return "Низька"