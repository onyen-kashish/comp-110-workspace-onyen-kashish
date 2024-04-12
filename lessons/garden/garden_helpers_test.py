"""Some test cases for my garden plan!"""

__author__ = "730578465"

import pytest
from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


# Test cases for add_by_kind function
def test_add_by_kind_use_case():
    """Test adding a new plant kind."""
    by_kind = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    add_by_kind(by_kind, "fruit", "apple")
    assert by_kind == {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"], "fruit": ["apple"]}


def test_add_by_kind_edge_case():
    """Test adding a plant kind that already exists."""
    by_kind = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    add_by_kind(by_kind, "flower", "rose")
    assert by_kind == {"flower": ["marigold", "zinnia", "rose"], "vegetable": ["carrots"]}


# Test cases for add_by_date function
def test_add_by_date_use_case():
    """Test adding a new plant to a specific date."""
    by_date = {"April": ["marigold"], "June": ["carrots"]}
    add_by_date(by_date, "April", "daisy")
    assert by_date == {"April": ["marigold", "daisy"], "June": ["carrots"]}


def test_add_by_date_edge_case():
    """Test adding a plant to a date that already exists."""
    by_date = {"April": ["marigold"], "June": ["carrots"]}
    add_by_date(by_date, "April", "rose")
    assert by_date == {"April": ["marigold", "rose"], "June": ["carrots"]}


# Test cases for lookup_by_kind_and_date function
def test_lookup_by_kind_and_date_use_case():
    """Test looking up plants of a specific kind to plant in a specific month."""
    plants_by_kind = {"flower": ["marigold", "daisy"], "vegetable": ["carrots"]}
    plants_by_date = {"April": ["marigold", "daisy"], "June": ["carrots"]}
    assert lookup_by_kind_and_date(plants_by_kind, plants_by_date, "flower",
                                   "April") == "flowers to plant in April: ['marigold', 'daisy']"


def test_lookup_by_kind_and_date_edge_case():
    """Test looking up plants of a specific kind to plant in a month where none should be planted."""
    plants_by_kind = {"flower": ["marigold", "daisy"], "vegetable": ["carrots"]}
    plants_by_date = {"April": ["marigold", "daisy"], "June": ["carrots"]}
    assert lookup_by_kind_and_date(plants_by_kind, plants_by_date, "vegetable",
                                   "April") == "No vegetables to plant in April"


# def test_lookup_by_kind_and_date():
#     by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
#     by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots", "marigold", "zinnia"]}
#     print(lookup_by_kind_and_date(by_kind, by_date, "flower", "June"))
#     print(lookup_by_kind_and_date(by_kind, by_date, "flower", "June"))
