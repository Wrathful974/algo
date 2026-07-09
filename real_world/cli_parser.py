import argparse


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Start a simple server")
    parser.add_argument("--port", default="8080")  # BUG: missing type=int
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args(argv)


def get_next_port(argv=None):
    """Return the port to use, offset by 1 (e.g. for a companion admin port)."""
    args = parse_args(argv)
    return args.port + 1  # crashes: TypeError, str + int
