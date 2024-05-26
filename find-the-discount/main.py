def dis(price, discount):
    discounted = price - price * discount / 100
    final = round(discounted, 2)
    return final

# round() Parameters
# The round() function takes two parameters:

# number - the number to be rounded.
# ndigits (optional) - number up to which the given number is rounded; defaults to 0.