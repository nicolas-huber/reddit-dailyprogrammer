# Simplify a given fraction by dividing nominator p and denominator q by their greatest common divisor (gcd)
# challenge url: "https://www.reddit.com/r/dailyprogrammer/comments/4uhqdb/20160725_challenge_277_easy_simplifying_fractions/"

# process user input
input_string = raw_input("Enter nominator and denominator (space separated): ")
input_string_split = input_string.split(" ")
p = int(input_string_split[0])
q = int(input_string_split[1])

# implement Euclid's algorithm
# observation: the greatest common divisor of two numbers also divides their difference
#
# example: nom = 48; denom = 18
# 48/18 = 2
# 48%18 = 12
# 18/12 = 1
# 18%12 = 6
# 12/6 = 2
# 12%6 = 0
# => 6 is greatest common divisor

# find greatest common divisor
def gcd(p, q):
    if p%q == 0:
        gcd = q
        return gcd
    else:
        while True:
            mod = p%q
            p, q = q, mod
            if p%q == 0:
                return mod
                break
   
print("{0} {1}".format(p/gcd(p, q), q/gcd(p, q)))
