"""Minimal tests."""

from scope_base import Item, parse


def test_item_holds_values():
    it = Item(key="a", value="b")
    assert it.key == "a"
    assert it.value == "b"


def test_parse_defaults():
    args = parse([])
    assert args.key == ""
    assert args.verbose is False
