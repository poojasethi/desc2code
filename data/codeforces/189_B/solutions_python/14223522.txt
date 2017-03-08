def main():
    (h, w) = map(int, raw_input().split())
    print (h/2)*(h-h/2)*(w/2)*(w-w/2)


if __name__ == '__main__':
    main()
