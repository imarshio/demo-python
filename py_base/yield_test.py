def test(num: int):
    if num == 0:
        yield f"now num is 0"
    if num == 0:
        yield f"now num is 1"
    if num == 1:
        yield f"now num is 1"
    yield f"now num is not 0 or 1"


if __name__ == "__main__":
    num0 = test(0)
    print(type(num0))
    print(next(num0))
    print(next(num0))
    print(next(num0))
    print("====")
    num1 = test(1)
    print(next(num1))
    num_other = test(11)
    print(next(num_other))
