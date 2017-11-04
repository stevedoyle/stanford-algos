
def count_inv(data):
    d, count = mergesort_and_count(data)
    return count


def mergesort_and_count(data):
    n = len(data)
    if n == 1:
        return data, 0
    mid = int(n/2)
    a, x = mergesort_and_count(data[:mid])
    b, y = mergesort_and_count(data[mid:])
    c, z = merge_and_count_inv(a, b)
    return (c, (x + y + z))


def merge_and_count_inv(a, b):
    n = len(a) + len(b)
    c = [0] * n
    i, j = 0, 0
    inv = 0
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
            inv += len(a[i:])
    return c, inv


if __name__ == '__main__':
    data = []
    with open('IntegerArray.txt') as f:
        for line in f:
            data.append(int(line.strip()))

    print(len(data))

    count = count_inv(data)

    print('Inversion count = ', count)
