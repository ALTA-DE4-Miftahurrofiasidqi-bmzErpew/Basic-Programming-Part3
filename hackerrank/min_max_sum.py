def miniMaxSum(arr):
    min = 0
    max = 0

    for _, v in enumerate(arr):
        if i == 0:
            min = v
            max = v
        else:
            if v < min:
                min = v
            if v > max:
                max = v
    print(sum(arr) - max, sum(arr) - min)


miniMaxSum([1, 2, 3, 4, 10])

# https://www.hackerrank.com/challenges/one-month-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
