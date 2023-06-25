from yogi import tokens, read

def falta(nums: set[int], n: int) -> int:
    for i in range(1, n + 1):
        if i not in nums:
            return i
    

def main():
    for n in tokens(int):
        k = read(int)
        nums: set[int] = {read(int) for _ in range(k)}
        print(falta(nums, n))


if __name__ == "__main__":
    main()