"""Shoelace Formula (Surveyor's Formula) Template.

Calculates the exact area of any simple (non-intersecting) polygon 
given its 2D vertex coordinates in consecutive order.
"""

def shoelace_area(vertices: list[tuple[int, int]]) -> float:
    """Calculates the exact floating-point area of a polygon.
    
    Args:
        vertices (list[tuple]): List of (x, y) coordinates [(x1, y1), (x2, y2), ...]
        
    Returns:
        float: The exact area of the polygon.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n: int = len(vertices)
    if n < 3:
        return 0.0

    area: float = 0.0
    for i in range(n):
        x1: int
        y1: int
        x1, y1 = vertices[i]
        
        x2: int
        y2: int
        x2, y2 = vertices[(i + 1) % n]
        
        # 2D Cross product
        area += (x1 * y2) - (x2 * y1)
        
    return abs(area) / 2.0


def shoelace_area_double(vertices: list[tuple[int, int]]) -> int:
    """Calculates exactly 2 * Area of the polygon using integer arithmetic.
    
    Use this when input coordinates are integers to strictly avoid 
    floating-point inaccuracies (e.g., when applying Pick's Theorem 
    or checking if an area is even/odd).
    
    Args:
        vertices (list[tuple]): List of integer (x, y) coordinates.
        
    Returns:
        int: Twice the area of the polygon.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n: int = len(vertices)
    if n < 3:
        return 0

    area: int = 0
    for i in range(n):
        x1: int
        y1: int
        x1, y1= vertices[i]

        x2: int
        y2: int
        x2, y2 = vertices[(i + 1) % n]
        
        area += (x1 * y2) - (x2 * y1)
        
    return abs(area)
