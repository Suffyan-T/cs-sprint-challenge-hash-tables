# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}

    for x in files:
        key = x.rsplit('/', 1)[1] 
        value = x

        if key not in cache:
            cache[key] = []
        cache[key].append(x)


    for y in queries:
        if y in cache:
            result += cache[y]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
