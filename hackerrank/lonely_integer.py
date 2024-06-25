def lonelyinteger(a):
    result = 0
    for i in a:
        result = result ^ i
    return result


x = lonelyinteger(
    [
        1,
        2,
        3,
        4,
        3,
        2,
        1,
    ]
)
print(x)


# https://www.hackerrank.com/challenges/one-month-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
