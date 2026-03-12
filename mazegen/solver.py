"""BFS-based maze solver for the A-Maze-ing project."""


def solve(
    grid: list[list[int]],
    entry: tuple[int, int],
    exit: tuple[int, int],
) -> str:
    """Solve the maze using breadth-first search (BFS).

    Finds the shortest path from entry to exit through the maze
    and returns it as a string of cardinal directions.

    Args:
        grid: A 2D list of integers encoding wall presence per cell
            using bitflags (N=1, E=2, S=4, W=8).
        entry: Tuple of (row, col) for the maze entry point.
        exit: Tuple of (row, col) for the maze exit point.

    Returns:
        A string of directions using the characters N, E, S, W
        representing the path from entry to exit.
    """
    pass
