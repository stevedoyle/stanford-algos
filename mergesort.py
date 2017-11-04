

def mergesort(data):
    n = len(data)
    if n == 1:
        return data
    mid = int(n/2)
    a = mergesort(data[:mid])
    b = mergesort(data[mid:])
    c = merge(a, b)
    return c


def merge(a, b):
    n = len(a) + len(b)
    c = [0] * n
    i, j = 0, 0
    for k in range(n):
        if i == len(a):
            c[k:] = b[j:]
            break
        if j == len(b):
            c[k:] = a[i:]
            break

        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
    return c


if __name__ == '__main__':
    data = [1, 5, 3, 7, 4, 8, 9, 5, 4, 2, 6, 1]
    sorteddata = mergesort(data)

    if sorteddata != sorted(data):
        print("Incorrect result")

    print(mergesort(data))
