import argparse


def parse_args() -> argparse.ArgumentParser:
    return argparse.ArgumentParser(
        prog="ProgramName",
        description="What the program does",
        epilog="Text at the bottom of help",
    )
