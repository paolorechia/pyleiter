from pyleiter.cli import parse_args
from pyleiter.runner import hello_world


if __name__ == "__main__":
    parse_args()
    print(hello_world())
