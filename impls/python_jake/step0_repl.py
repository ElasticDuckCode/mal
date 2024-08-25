import os
import readline
import atexit


def mal_read(input):
    return input


def mal_eval(input):
    return input


def mal_print(input):
    print(input)
    return


def mal_rep(rep_input):
    read_result = mal_read(rep_input)
    eval_result = mal_eval(read_result)
    print_result = mal_print(eval_result)
    return print_result


def main():
    # Create readline buffer for better repl interaction
    histfile = os.path.join(os.path.expanduser('~'), ".mal_history")

    try:
        # If file doesn't exist, this would create it.
        open(histfile, 'a').close()
        readline.read_history_file(histfile)
        readline.set_history_length(1_000)
        readline.parse_and_bind("")
    except FileNotFoundError:
        pass

    try:
        while 1:
            line = input("user> ")

            if line == 'exit':
                break

            mal_rep(line)

    except KeyboardInterrupt:
        # Pass keyboard interupt after writing history file to disk.
        pass

    atexit.register(readline.write_history_file, histfile)
    return 0


if __name__ == "__main__":
    main()
