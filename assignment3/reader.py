# GEO1000 - Assignment 3
# Authors: Joost de Witte & Daan Noordam
# Studentnumbers: 5656176 & 5148766

from geometry import Point, Rectangle, Circle
from strips import StripStructure


def read(file_nm, no_strips):
    """Reads a file with on the first uncommented line a bbox 
    (4 numbers separated by a space) and subsequently 0 or more lines with 
    points (2 numbers separated by a space) into a Strip Structure.

    If no valid box is found in the input file, it returns None.
    Otherwise a StripStructure with 0 or more points is returned.

    Returns - None or a StripStructure instance
    """
    try:
        with open(file_nm, 'r') as points_file:
            lines = []  #
            for line in points_file:
                if not line.startswith('#'):
                    lines.append(line)  # append only the non-commented lines
    except FileNotFoundError:
        print('File not found.')

    # Check is there is any lines left after removing comments
    if len(lines) == 0:
        return None

    # First line is now the bbox, check if format is correct and define extent and
    if len(lines[0].split()) != 4:  # should result in list of 4
        return None

    ll_point = Point(float(lines[0].split()[0]), float(lines[0].split()[1]))
    ur_point = Point(float(lines[0].split()[2]), float(lines[0].split()[3]))
    extent = Rectangle(ll_point, ur_point)

    # Initialising strip_structure with extent of bbox, no_strips passed from query.py
    strip_structure = StripStructure(extent, no_strips)

    # From line 1 onwards, all lines should be points
    for line in lines[1:]:
        if len(line.split()) != 2:
            continue  # Skip this iteration (invalid format of point)

        # initialise point and append it to the strip_structure
        pt = Point(float(line.split()[0]), float(line.split()[1]))
        strip_structure.append_point(pt)

    return strip_structure


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
