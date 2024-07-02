from pyleiter.cli import build_arg_parser, hello_world


if __name__ == "__main__":
    arg_parser = build_arg_parser()
    args = arg_parser.parse_args()
    print(hello_world())
