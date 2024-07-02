from pyleiter.runner import run_process
import argparse


def build_arg_parser() -> argparse.ArgumentParser:
    return argparse.ArgumentParser(
        prog="pyleiter",
        description="Simple task management for a Python project",
        epilog="Enjoy!",
    )


def run_command(command: str):
    return run_process(command)


def hello_world():
    return "hello world"
