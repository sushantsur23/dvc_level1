import os


def main():
    print("Always run")
    with open(os.path.join("rough","test.txt"), "W") as f:
        f.write("This is a test file")

if __name__=='__main__':
    main()

