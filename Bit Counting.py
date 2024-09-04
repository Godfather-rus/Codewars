def count_bits(n):
    return len([a for a in bin(n) if a == "1"])

if __name__ == '__main__':
    print(count_bits(1234))

def countBits2(n):
    return bin(n).count("1")
    