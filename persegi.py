def calculate_area(side_length):
    """Calculate the area of a square."""
    return side_length ** 2

def calculate_perimeter(side_length):
    """Calculate the perimeter of a square."""
    return 4 * side_length

def calculate_diagonal(side_length):
    """Calculate the diagonal of a square."""
    return (2 ** 0.5) * side_length

# Example usage:
if __name__ == '__main__':
    side = 5
    print(f"Area: {calculate_area(side)}")
    print(f"Perimeter: {calculate_perimeter(side)}")
    print(f"Diagonal: {calculate_diagonal(side)}")