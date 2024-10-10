# GEO1000 - Assignment 3
# Authors: Joost de Witte & Daan Noordam
# Studentnumbers: 5656176 & 5148766

from geometry import Point, Rectangle


class Strip:
    def __init__(self, rectangle):
        """Constructor. Inits a Strip instance with a Rectangle describing 
        its shape and an empty points list.
        """
        self.rect = rectangle
        self.points = []


class StripStructure:
    def __init__(self, extent, no_strips):
        """Constructor. Inits a StripStructure instance with the correct
        number of Strip instances and makes sure that the domain is 
        correctly divided over the strips.
        """
        self.strips = []
        # Extend this method,
        # so that the right number of strip objects (with the correct extent)
        # are appended to the strips list
        total_width = extent.width()  # from geometry.py
        strip_width = total_width / no_strips
        for i in range(no_strips):
            ll_x = extent.ll.x + i * strip_width  # left x boundary of the strip
            ur_x = ll_x + strip_width  # right x boundary of strip
            # Use geometry.py objects to create a new Strip and append the strip to list
            strip = Strip(Rectangle(Point(ll_x, extent.ll.y), Point(ur_x, extent.ur.y)))
            self.strips.append(strip)

    def find_overlapping_strips(self, shape):
        """Returns a list of strip objects for which their rectangle intersects 
        with the shape given.

        Returns - list of Strips
        """
        overlapping_strips = []
        for strip in self.strips:
            # apply geometry.py intersect on the strip and shape given
            if strip.rect.intersects(shape):
                overlapping_strips.append(strip)
        return overlapping_strips

    def query(self, shape):
        """Returns a list of points that overlaps the given shape.

        For this it first finds the strips that overlap the shape,
        using the find_overlapping_strips method.

        Then, all points of the selected strips are checked for intersection
        with the query shape.

        Returns - list of Points
        """
        overlapping_strips = self.find_overlapping_strips(shape)  # list with strips that overlap with shape
        result = []  # all overlapping points

        for strip in overlapping_strips:
            # Append points that intersect with the shape into list
            for point in strip.points:
                if point.intersects(shape):
                    result.append(point)
        return result

    def append_point(self, pt):
        """Appends a point object to the list of points of the correct strip
        (i.e. the strip the Point intersects).

        For this it first finds the strips that overlap the point,
        using the find_overlapping_strips method.

        In case multiple strips overlap the point, the point is added
        to the strip with the left most coordinate.

        Returns - None
        """
        overlapping_strips = self.find_overlapping_strips(pt)  # list with strips that overlap with pt

        # Maximum of two strips can intersect with 1 point, two possible cases: len(overlap...) = 1 or = 2.
        # If 1, the point is added to the strip. If 2, point is on the seam, it is added to the left most strip
        if len(overlapping_strips) == 1:
            overlapping_strips[0].points.append(pt)
        elif len(overlapping_strips) == 2:
            # leftmost_strip is determined by ll.x coordinate
            if overlapping_strips[0].rect.ll.x < overlapping_strips[1].rect.ll.x:
                leftmost_strip = overlapping_strips[0]
            else:
                leftmost_strip = overlapping_strips[1]
            leftmost_strip.points.append(pt)
        else:
            print("Error: Point is in none of the strips")

    def print_strip_statistics(self):
        """Prints:
        * how many strips there are in the structure

        And then, for all the strips in the structure:
        * an id (starting at 1),
        * the number of points in a strip, 
        * the lower left point of a strip and 
        * the upper right point of a strip.

        Returns - None
        """
        # As per sample run template in the assignment
        print(f"{len(self.strips)} strips")

        strip_nr = 1  # init strip number counter

        for strip in self.strips:
            points_amount = len(strip.points)
            ll = strip.rect.ll
            ur = strip.rect.ur

            # Print the statistics for the current strip in the sample run format
            print(f"#{strip_nr} with {points_amount} points, ll: POINT ({ll.x} {ll.y}), ur: POINT ({ur.x} {ur.y})")

            # Increment the strip counter for the next strip
            strip_nr += 1

    def dumps_strips(self):
        """Dumps the strips of this structure to a str, 
        which (if saved in a text file) can be loaded as 
        delimited text layer in QGIS.

        Returns - str
        """
        lines = "strip;wkt\n"
        for i, strip in enumerate(self.strips, start=1):
            t = "{0};{1}\n".format(i, strip.rect)
            lines += t
        return lines

    def dumps_points(self):
        """Dumps the points of this structure to a str, 
        which (if saved in a text file) can be loaded as 
        delimited text layer in QGIS.

        Returns - str
        """
        lines = "strip;wkt\n"
        for i, strip in enumerate(self.strips, start=1):
            for pt in strip.points:
                t = "{0};{1}\n".format(i, pt)
                lines += t
        return lines
