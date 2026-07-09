import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from real_world.cli_parser import get_next_port


def test_default_port_is_int():
    assert get_next_port([]) == 8081


def test_custom_port_is_int():
    assert get_next_port(["--port", "9000"]) == 9001
