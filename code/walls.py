
class Wall:

    def __init__(self, reference=None):
        self.reference = reference #x, y and z of the floor
        #A for iteration for each one of the seven parts that compose the wall
        self.sub_part_half_width = [0.1, 7.0, 0.1, 0.1, 1.0, 0.1, 1.0, 0.1,
                                    0.1, 0.5, 0.1, 0.5, 0.1, 0.1, 1.0,
                                    0.1, 1.75, 0.1, 0.1, 1.5, 0.1, 0.5,
                                    0.5, 0.1, 1, 0.1, 0.1, 0.1, 0.20, 0.20,
                                    0.20, 0.20, 0.20, 0.20, 0.20, 1.5,
                                    2.5, 0.1, 3, 0.1, 0.1, 2.5, 1.5, 1.5, 0.1,
                                    3, 0.1, 1.5, 0.1, 0.1, 0.1, 0.1, 0.1]
        self.sub_part_half_height = [5.0, 5.0, 5.0, 1.0, 1.0, 1.0, 1.0, 2.0,
                                    2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0,
                                    2.0, 2.0, 2.0, 2.0, 2, 2, 2,
                                    2, 2, 2, 2, 2, 2, 2, 2,
                                    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                                    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        self.sub_part_half_depth = [20.0, 0.1, 20.0, 1.0, 0.1, 1.0, 0.1, 3.1,
                                    1.1, 0.1, 2.1, 0.1, 1.6, 3.1, 0.1,
                                    1.85, 0.1, 2.1, 3.6, 0.1, 0.6, 0.1,
                                    0.1, 2, 0.1, 1.1, 2.1, 2.1, 0.1, 0.1,
                                    0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 5.6,
                                    0.1, 1, 1.5, 0.1, 0.1, 0.1, 5.6, 0.1, 1.6,
                                    0.1, 1, 1, 1.5, 1, 1]
        self.sub_part_center = self.__get_sub_part_center(self.reference)
        self.wall = []

        self.__generate_coordinates()

    def __get_sub_part_center(self, reference):
        sub_part_center = [
                        (reference[0] - 7.1, reference[1] + 5, reference[2] + 0),
                        (reference[0] + 0.0, reference[1] + 5, reference[2] - 20.1),
                        (reference[0] + 7.1, reference[1] + 5, reference[2] + 0),
                        (reference[0] - 1, reference[1] + 11, reference[2] + 17),
                        (reference[0] + 0.0, reference[1] + 11, reference[2] + 16),
                        (reference[0] + 1, reference[1] + 11, reference[2] + 17),
                        (reference[0] + 0.0, reference[1] + 11, reference[2] + 18),
                        (reference[0] + 4, reference[1] + 1.9, reference[2] + 15), #BEGIN INTERNALS
                        (reference[0] + 1, reference[1] + 1.9, reference[2] + 17),
                        (reference[0] + 1.5, reference[1] + 1.9, reference[2] + 16),
                        (reference[0] + 2, reference[1] + 1.9, reference[2] + 14),
                        (reference[0] + 1.5, reference[1] + 1.9, reference[2] + 12),
                        (reference[0] + 1, reference[1] + 1.9, reference[2] + 13.5),
                        (reference[0] - 1, reference[1] + 1.9, reference[2] + 15),
                        (reference[0] - 2, reference[1] + 1.9, reference[2] + 12),
                        (reference[0] - 4, reference[1] + 1.9, reference[2] + 16.25),
                        (reference[0] - 2.75, reference[1] + 1.9, reference[2] + 16),
                        (reference[0] - 3, reference[1] + 1.9, reference[2] + 13),
                        (reference[0] - 4, reference[1] + 1.9, reference[2] + 10),
                        (reference[0] - 5.5, reference[1] + 1.9, reference[2] + 8),
                        (reference[0] - 2, reference[1] + 1.9, reference[2] + 11.5),
                        (reference[0] - 1.5, reference[1] + 1.9, reference[2] + 11),
                        (reference[0] - 1.5, reference[1] + 1.9, reference[2] + 10),
                        (reference[0] - 1, reference[1] + 1.9, reference[2] + 9),
                        (reference[0] - 2, reference[1] + 1.9, reference[2] + 8),
                        (reference[0] - 3, reference[1] + 1.9, reference[2] + 9),
                        (reference[0] + 1, reference[1] + 1.9, reference[2] + 9),
                        (reference[0] + 4, reference[1] + 1.9, reference[2] + 9),
                        (reference[0] - 6.9, reference[1] + 1.9, reference[2] + 16),
                        (reference[0] - 6.9, reference[1] + 1.9, reference[2] + 12),
                        (reference[0] - 4.1, reference[1] + 1.9, reference[2] + 12),
                        (reference[0] + 4.1, reference[1] + 1.9, reference[2] + 11),
                        (reference[0] + 6.9, reference[1] + 1.9, reference[2] + 11),
                        (reference[0] + 4.1, reference[1] + 1.9, reference[2] + 8),
                        (reference[0] + 6.9, reference[1] + 1.9, reference[2] + 8),
                        (reference[0] - 5.5, reference[1] + 1.9, reference[2] + 5),
                        (reference[0] + 4.5, reference[1] + 1.9, reference[2] + 5),
                        (reference[0] - 4, reference[1] + 1.9, reference[2] + 0.5),
                        (reference[0] - 4, reference[1] + 1.9, reference[2] - 5),
                        (reference[0] + 2, reference[1] + 1.9, reference[2] + 4),
                        (reference[0] + 2, reference[1] + 1.9, reference[2] + 0.5),
                        (reference[0] + 4.5, reference[1] + 1.9, reference[2] + 0),
                        (reference[0] - 5.5, reference[1] + 1.9, reference[2] + 0),
                        (reference[0] - 5.5, reference[1] + 1.9, reference[2] - 2),
                        (reference[0] - 1, reference[1] + 1.9, reference[2] + 0.5),
                        (reference[0] + 4, reference[1] + 1.9, reference[2] - 5),
                        (reference[0] + 2, reference[1] + 1.9, reference[2] - 3.5),
                        (reference[0] + 5.5, reference[1] + 1.9, reference[2] - 2),
                        (reference[0] + 4, reference[1] + 1.9, reference[2] - 4),
                        (reference[0] + 1, reference[1] + 1.9, reference[2] + 5),
                        (reference[0] + 1, reference[1] + 1.9, reference[2] + 1.5),
                        (reference[0] - 2, reference[1] + 1.9, reference[2] + 4),
                        (reference[0] - 2, reference[1] + 1.9, reference[2] + 1)
                        ]
        return sub_part_center

    def __gen_vertexes(self, i):
        # a, b, c, d, e and f vertices
        a = (
            self.reference[0] - self.sub_part_half_width[i] + self.sub_part_center[i][0] ,
            self.reference[1] + self.sub_part_center[i][1] - self.sub_part_half_height[i],
            self.reference[2] + self.sub_part_half_depth[i] + self.sub_part_center[i][2]
        )

        b = (
            self.reference[0] + self.sub_part_half_width[i] + self.sub_part_center[i][0],
            self.reference[1] + self.sub_part_center[i][1] - self.sub_part_half_height[i],
            self.reference[2] + self.sub_part_half_depth[i] + self.sub_part_center[i][2]
        )

        c = (
            self.reference[0] + self.sub_part_half_width[i] + self.sub_part_center[i][0] ,
            self.reference[1] + self.sub_part_center[i][1] + self.sub_part_half_height[i],
            self.reference[2] + self.sub_part_half_depth[i] + self.sub_part_center[i][2]
        )

        d = (
            self.reference[0] - self.sub_part_half_width[i] + self.sub_part_center[i][0] ,
            self.reference[1] + self.sub_part_center[i][1] + self.sub_part_half_height[i],
            self.reference[2] + self.sub_part_half_depth[i] + self.sub_part_center[i][2]
        )

        e = (
            self.reference[0] - self.sub_part_half_width[i] + self.sub_part_center[i][0] ,
            self.reference[1] + self.sub_part_center[i][1] - self.sub_part_half_height[i],
            self.reference[2] - self.sub_part_half_depth[i] + self.sub_part_center[i][2]
        )

        f = (
            self.reference[0] + self.sub_part_half_width[i] + self.sub_part_center[i][0] ,
            self.reference[1] + self.sub_part_center[i][1] - self.sub_part_half_height[i],
            self.reference[2] - self.sub_part_half_depth[i] + self.sub_part_center[i][2]
        )

        g = (
            self.reference[0] + self.sub_part_half_width[i] + self.sub_part_center[i][0] ,
            self.reference[1] + self.sub_part_center[i][1] + self.sub_part_half_height[i],
            self.reference[2] - self.sub_part_half_depth[i] + self.sub_part_center[i][2]
        )

        h = (
            self.reference[0] - self.sub_part_half_width[i] + self.sub_part_center[i][0] ,
            self.reference[1] + self.sub_part_center[i][1] + self.sub_part_half_height[i],
            self.reference[2] - self.sub_part_half_depth[i] + self.sub_part_center[i][2]
        )

        return a, b, c, d, e, f, g, h

    def __generate_coordinates(self):

        # For loop to generate all the coordinates of the wall parts

        for i in range(len(self.sub_part_half_height)):
            sub_part = []

            a, b, c, d, e, f, g, h = self.__gen_vertexes(i)

            # This vector stores the vertices of the front face of the sub_part part of the wall
            sub_part_front = (a,b,c,d)
            sub_part.append(sub_part_front)

            # This vector stores the vertices of the sub_part face of the sub_part part of the wall
            sub_part_back = (e,f,g,h)
            sub_part.append(sub_part_back)

            # This vector stores the vertices of the right face of the sub_part part of the wall
            sub_part_right = (b,f,g,c)
            sub_part.append(sub_part_right)

            # This vector stores the vertices of the left face of the sub_part part of the wall
            sub_part_left = (e,a,d,h)
            sub_part.append(sub_part_left)

            # This vector stores the vertices of the top face of the sub_part part of the wall
            sub_part_top = (c,g,h,d)
            sub_part.append(sub_part_top)

            # This vector stores the vertices of the bottom face of the sub_part part of the wall
            sub_part_bottom = (a,e,f,b)
            sub_part.append(sub_part_bottom)

            self.wall.append(sub_part)

    def get_wall(self):
            return self.wall

