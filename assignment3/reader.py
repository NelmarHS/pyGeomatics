# GEO1000 - Assignment 3
# Authors:
# Studentnumbers:

from geometry import Point, Rectangle, Circle
from strips import StripStructure

file_nm = open("points1.txt")
print(file_nm.readline())
def read(file_nm, no_strips):
    """Reads a file with on the first uncommented line a bbox 
    (4 numbers separated by a space) and subsequently 0 or more lines with 
    points (2 numbers separated by a space) into a Strip Structure.

    If no valid box is found in the input file, it returns None.
    Otherwise a StripStructure with 0 or more points is returned.

    Returns - None or a StripStructure instance
    """
    file_nm.readline(1)


def dump(structure, strip_file_nm="strips.wkt", point_file_nm="points.wkt"):
    """Dump the contents of a strip structure to 2 files that can be opened
    with QGIS.

    Returns - None
    """
    with open(strip_file_nm, "w") as fh:
        fh.write(structure.dump_strips())
    with open(point_file_nm, "w") as fh:
        fh.write(structure.dump_points())


def _test():
    """You can use this function to test whether 
    the read and dump functions work correctly.
    """
    pass


if __name__ == "__main__":
    _test()
