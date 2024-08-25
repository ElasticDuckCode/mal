def mal_read(input):
    return input


def mal_eval(input):
    return input


def mal_print(input):
    return input


def mal_rep(rep_input):
    read_result = mal_read(rep_input)
    eval_result = mal_eval(read_result)
    print_result = mal_print(eval_result)
    return print_result


def main():
    while 1:
        line = input("user> ")
        result = mal_rep(line)
        print(result)
    return 0


if __name__ == "__main__":
    main()
