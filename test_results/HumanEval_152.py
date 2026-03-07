def compare(game, guess):
    return [0 if g == h else abs(g - h) for g, h in zip(game, guess)]