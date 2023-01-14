class StrokeHelper:
    """Helper class for stroke operations."""

    def __init__(self, context, stroke, stroke_index, mode="DRAW"):
        """Initialize the helper class.

        :param context: The context to use.
        :param stroke: The stroke to use.
        :param stroke_index: The index of the stroke.
        :param mode: The mode to use.
        """
        self.context = context
        self.stroke = stroke
        self.stroke_index = stroke_index
        self.mode = mode

    def get_stroke_points(self):
        """Get the stroke points.

        :return: The stroke points.
        """
        return self.stroke.points

    def get_stroke_points_count(self):
        """Get the stroke points count.

        :return: The stroke points count.
        """
        return len(self.stroke.points)

    def get_stroke_point(self, index):
        """Get the stroke point at the given index.

        :param index: The index of the point to get.
        :return: The stroke point.
        """
        return self.stroke.points[index]

    def get_stroke_point_co(self, index):
        """Get the stroke point coordinate at the given index.

        :param index: The index of the point to get.
        :return: The stroke point coordinate.
        """
        return self.stroke.points[index].co

    def get_stroke_point_pressure(self, index):
        """Get the stroke point pressure at the given index.

        :param index: The index of the point to get.
        :return: The stroke point pressure.
        """
        return self.stroke.points[index].pressure

    def get_stroke_point_strength(self, index):
        """Get the stroke point strength at the given index.

        :param index: The index of the point to get.
        :return: The stroke point strength.
        """
        return self.stroke.points[index].strength

    def get_stroke_point_uv(self, index):
        """Get the stroke point uv at the given index.

        :param index: The index of the point to get.
        :return: The stroke point uv.
        """
        return self.stroke.points[index].uv

    def get_stroke_point_uv_rotation(self, index):
        """Get the stroke point uv rotation at the given index.

        :param index: The index of the point to get.
        :return: The stroke point uv rotation.
        """
        return self.stroke
