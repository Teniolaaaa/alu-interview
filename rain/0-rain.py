#!/usr/bin/python3
"""
Module for calculating rainwater retention between walls.
"""


def rain(walls):
    """
    Calculate how many square units of water will be retained after it rains.

    Args:
        walls: A list of non-negative integers representing wall heights.

    Returns:
        Integer indicating total amount of rainwater retained.
        Returns 0 if the list is empty.
    """
    if not walls or len(walls) < 3:
        return 0

    n = len(walls)
    water = 0

    # Precompute maximum height to the left of each position
    left_max = [0] * n
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Precompute maximum height to the right of each position
    right_max = [0] * n
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate trapped water at each position
    for i in range(n):
        water += min(left_max[i], right_max[i]) - walls[i]

    return water
