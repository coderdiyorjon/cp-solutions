"""Polygon Area calulation using the Shoelace Formula.

Calculates the area of any simple (non-self-intersecting) polygon
given its vertices in consecutive order (either clockwise or counter-clockwise).
"""

def polygon_area(points: list[tuple[int, int]]) -> float:
    """Calculates the exact area of a polygon.
    
    Args:
        points (list): List of (x, y) coordinates [(x1, y1), (x2, y2), ...]
        
    Returns:
        float: The exact area of the polygon.
    Time Complexity: O(N)
    """
    n: int = len(points)
    area: float = 0.0
    
    for i in range(n):
        x1: int
        y1: int
        x1, y1 = points[i]
        # (i + 1) % n cleanly wraps the last point back to the first
        x2: int
        y2: int
        x2, y2 = points[(i + 1) % n]
        
        # 2D Cross product logic
        area += (x1 * y2) - (x2 * y1)
        
    return abs(area) / 2.0


def polygon_area_double(points: list[tuple[int, int]]) -> int:
    """Calculates exactly 2 * Area of the polygon.
    
    Use this when input coordinates are integers and you want to strictly
    avoid floating-point inaccuracies. If the problem asks for the area
    as an intger (or if you need to check if the area is odd/even),
    this guarantees flawless precision.
    
    Returns:
        int: Twise the area of the polygon.
    Time Complexity: O(N)
    """
    n: int = len(points)
    area: int = 0
    
    for i in range(n):
        x1: int
        y1: int
        x1, y1 = points[i]
        
        x2: int
        y2: int
        x2, y2 = points[(i + 1) % n]
        
        area += (x1 * y2) - (x2 * y1)
    
    return abs(area)

  