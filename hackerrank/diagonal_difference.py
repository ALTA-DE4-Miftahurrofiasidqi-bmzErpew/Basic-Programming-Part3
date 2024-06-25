def diagonalDifference(arr):
    left = 0
    right = 0
    for i, v in enumerate(arr):
        for item, value in enumerate(v):
            if i == item:
                left += value

            if len(v) - 1 - i == item:
                right += value

    return abs(left - right)


matrix_x = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12],
]
print(diagonalDifference(matrix_x))

# https://hackerrank.com/challenges/one-month-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
