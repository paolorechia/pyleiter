from pyleiter.config import read_pyleiter_config
from pyleiter.runner import run_process
import argparse


def _build_arg_parser(config) -> argparse.ArgumentParser:
    return argparse.ArgumentParser(
        prog="pyleiter",
        description="Simple task management for a Python project",
        epilog="Enjoy!",
    )


def _check_args(args):
    return False


def _run_command(command: str):
    return run_process(command)


def main():
    config = read_pyleiter_config()
    arg_parser = _build_arg_parser(config)
    args = arg_parser.parse_args()
    _check_args(args)
