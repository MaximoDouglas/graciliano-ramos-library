
class Table:


    def __init__(self, reference=None):
        self.reference = reference #x, y and z of the floor
        #A for iteration for each one of the seven parts that compose the table
        self.sub_part_half_width = [0.50, 0.01, 0.01, 0.01, 0.01]
        self.sub_part_half_height = [0.05, 0.325, 0.325, 0.325, 0.325]
        self.sub_part_half_depth = [0.50, 0.01, 0.01, 0.01, 0.01]
        self.sub_part_center = self.__get_sub_part_center(self.reference)
        self.table = []

        self.__generate_coordinates()

    def __get_sub_part_center(self, reference):
        sub_part_center = [
                        (reference[0] + 0.0, reference[1] + 0.70, reference[2] + 0),
                        (reference[0] + 0.49, reference[1] + 0.325, reference[2] - 0.49),
                        (reference[0] - 0.49, reference[1] + 0.325, reference[2] - 0.49),
                        (reference[0] + 0.49, reference[1] + 0.325, reference[2] + 0.49),
                        (reference[0] - 0.49, reference[1] + 0.325, reference[2] + 0.49)
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

        # For loop to generate all the coordinates of the table parts

        for i in range(len(self.sub_part_half_height)):
            sub_part = []

            a, b, c, d, e, f, g, h = self.__gen_vertexes(i)

            # This vector stores the vertices of the front face of the sub_part part of the table
            sub_part_front = (a,b,c,d)
            sub_part.append(sub_part_front)

            # This vector stores the vertices of the sub_part face of the sub_part part of the table
            sub_part_back = (e,f,g,h)
            sub_part.append(sub_part_back)

            # This vector stores the vertices of the right face of the sub_part part of the table
            sub_part_right = (b,f,g,c)
            sub_part.append(sub_part_right)

            # This vector stores the vertices of the left face of the sub_part part of the table
            sub_part_left = (e,a,d,h)
            sub_part.append(sub_part_left)

            # This vector stores the vertices of the top face of the sub_part part of the table
            sub_part_top = (c,g,h,d)
            sub_part.append(sub_part_top)

            # This vector stores the vertices of the bottom face of the sub_part part of the table
            sub_part_bottom = (a,e,f,b)
            sub_part.append(sub_part_bottom)

            self.table.append(sub_part)

    def get_table(self):
            return self.table
