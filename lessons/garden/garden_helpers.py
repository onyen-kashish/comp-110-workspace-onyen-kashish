"""Some functions for my garden plan!"""

__author__ = "730578465"


def add_by_kind(garden: dict[str, list[str]], new_plant_kind: str, new_plant: str) -> None:
    """Add plant under its kind."""
    if new_plant_kind in garden:  # if the kind is already in the dictionary ("flower" was in by_kind)
        garden[new_plant_kind].append(new_plant)
    else:  # if the kind is not in the dictionary
        garden[new_plant_kind] = []
        garden[new_plant_kind].append(new_plant)


def add_by_date(garden_by_month: dict[str, list[str]], month: str, plant: str) -> None:
    """Add plant under month to sow seeds"""
    if month in garden_by_month:
        garden_by_month[month].append(plant)
    else:
        garden_by_month[month] = []
        garden_by_month[month].append(plant)


def lookup_by_kind_and_date(by_kind: dict[str, list[str]], by_date: dict[str, list[str]], plant: str,
                            month: str) -> str:
    """Return string with list of plants of a specific kind to plant in a specific month."""
    assert plant in by_kind
    assert month in by_date
    plants_to_plant = []

    if plant in by_kind and month in by_date:
        for value in by_kind[plant]:
            for month_value in by_date[month]:
                if value == month_value:
                    plants_to_plant.append(value)

    if plants_to_plant:
        return f"{plant}s to plant in {month}: {plants_to_plant}"
    else:
        return f"No {plant}s to plant in {month}."
