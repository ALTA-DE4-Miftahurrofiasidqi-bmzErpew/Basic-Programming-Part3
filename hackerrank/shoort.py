def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Tentukan nilai maksimum dan minimum
    min_val, max_val = min(arr), max(arr)
    print(min_val, max_val)

    # # Tentukan jumlah bucket
    bucket_range = (max_val - min_val) / len(arr) + 1
    buckets = [[] for _ in range(len(arr))]
    print(bucket_range, buckets)

    # # Distribusikan elemen ke dalam bucket
    for num in arr:
        bucket_index = int((num - min_val) // bucket_range)
        buckets[bucket_index].append(num)
        # print(num)
        print(buckets)

    # # Urutkan setiap bucket dan gabungkan
    # sorted_array = []
    # for bucket in buckets:
    #     sorted_array.extend(sorted(bucket))

    # return sorted_array


arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)
