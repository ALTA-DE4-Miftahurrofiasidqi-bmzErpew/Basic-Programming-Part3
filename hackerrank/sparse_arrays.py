def machingStrings(strings, queries):
    result = []
    for query in queries:
        count = 0
        for string in strings:
            if string == query:
                count += 1
        result.append(count)
    return result


# https://www.hackerrank.com/challenges/one-month-preparation-kit-sparse-arrays/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
