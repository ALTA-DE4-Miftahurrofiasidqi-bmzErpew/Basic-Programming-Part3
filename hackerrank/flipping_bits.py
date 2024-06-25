def flippingBits(n):
    biner_32bit = "11111111111111111111111111111111"
    biner_n = bin(n)[2:]
    biner_n = biner_n.zfill(32)

    flip = n ^ int(biner_32bit, 2)

    return flip


x = flippingBits(9)
print(type(x), x)


# https://www.hackerrank.com/challenges/one-month-preparation-kit-flipping-bits/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
