def plusMinus(arr):
    # Write your code here
    p = 0
    n = 0
    z = 0

    for _, v in enumerate(arr):
        if v > 0:
            p += 1
        elif v < 0:
            n += 1
        else:
            z += 1
    count = len(arr)
    print(p / count)
    print(n / count)
    print(z / count)


# https://www.hackerrank.com/challenges/one-month-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
