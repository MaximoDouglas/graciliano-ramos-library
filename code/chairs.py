
class Chair:
    

    def __init__(self):
        self.referent = [0, 0, 0] #x, y and z of the floor
        #A for iteration for each one of the seven parts that compose the chair
        self.sub_part_half_width = [0.25, 0.05, 0.25, 0.01, 0.01, 0.01, 0.01]
        self.sub_part_half_height = [0.25, 0.10, 0.05, 0.2, 0.2, 0.2, 0.2]
        self.sub_part_half_depth = [0.05, 0.025, 0.25, 0.01, 0.01, 0.01, 0.01]
        self.sub_part_center = self.__get_sub_part_center(self.referent)
        self.chairs = []

        self.__generate_coordinates()

    def __get_sub_part_center(self, referent):
        sub_part_center = [
                        (referent[0] + 0.0, referent[1] + 0.85, referent[2] + 0.0),
                        (referent[0] + 0.0, referent[1] + 0.5, referent[2] - 0.025),
                        (referent[0] + 0.0, referent[1] + 0.45, referent[2] + 0.25),
                        (referent[0] + 0.24, referent[1] + 0.2, referent[2] + 0.01),
                        (referent[0] - 0.24, referent[1] + 0.2, referent[2] + 0.01),
                        (referent[0] + 0.24, referent[1] + 0.2, referent[2] + 0.49),
                        (referent[0] - 0.24, referent[1] + 0.2, referent[2] + 0.49)
                        ]
        return sub_part_center

    def __gen_vertexes(self, i):
        # a, b, c, d, e and f vertices
        a = (
            self.referent[0] - self.sub_part_half_width[i] + self.sub_part_center[i][0] ,
            self.referent[1] + self.sub_part_center[i][1] - self.sub_part_half_height[i],
            self.referent[2] + self.sub_part_half_depth[i] + self.sub_part_center[i][2]
        )

        b = (
            self.referent[0] + self.sub_part_half_width[i] + self.sub_part_center[i][0],
            self.referent[1] + self.sub_part_center[i][1] - self.sub_part_half_height[i],
            self.referent[2] + self.sub_part_half_depth[i] + self.sub_part_center[i][2]
        )

        c = (
            self.referent[0] + self.sub_part_half_width[i] + self.sub_part_center[i][0] ,
            self.referent[1] + self.sub_part_center[i][1] + self.sub_part_half_height[i],
            self.referent[2] + self.sub_part_half_depth[i] + self.sub_part_center[i][2]
        )

        d = (
            self.referent[0] - self.sub_part_half_width[i] + self.sub_part_center[i][0] ,
            self.referent[1] + self.sub_part_center[i][1] + self.sub_part_half_height[i],
            self.referent[2] + self.sub_part_half_depth[i] + self.sub_part_center[i][2]
        )

        e = (
            self.referent[0] - self.sub_part_half_width[i] + self.sub_part_center[i][0] ,
            self.referent[1] + self.sub_part_center[i][1] - self.sub_part_half_height[i],
            self.referent[2] - self.sub_part_half_depth[i] + self.sub_part_center[i][2]
        )

        f = (
            self.referent[0] + self.sub_part_half_width[i] + self.sub_part_center[i][0] ,
            self.referent[1] + self.sub_part_center[i][1] - self.sub_part_half_height[i],
            self.referent[2] - self.sub_part_half_depth[i] + self.sub_part_center[i][2]
        )

        g = (
            self.referent[0] + self.sub_part_half_width[i] + self.sub_part_center[i][0] ,
            self.referent[1] + self.sub_part_center[i][1] + self.sub_part_half_height[i],
            self.referent[2] - self.sub_part_half_depth[i] + self.sub_part_center[i][2]
        )

        h = (
            self.referent[0] - self.sub_part_half_width[i] + self.sub_part_center[i][0] ,
            self.referent[1] + self.sub_part_center[i][1] + self.sub_part_half_height[i],
            self.referent[2] - self.sub_part_half_depth[i] + self.sub_part_center[i][2]
        )

        return a, b, c, d, e, f, g, h

    def __generate_coordinates(self):

        # For loop to generate all the coordinates of the chair parts
        chair = []  # Just one for now

        for i in range(len(self.sub_part_half_height)):
            sub_part = []

            a, b, c, d, e, f, g, h = self.__gen_vertexes(i)

            # This vector stores the vertices of the front face of the sub_part part of the chair
            sub_part_front = (a,b,c,d)
            sub_part.append(sub_part_front)


            # This vector stores the vertices of the sub_part face of the sub_part part of the chair
            sub_part_back = (e,f,g,h)
            sub_part.append(sub_part_back)

            # This vector stores the vertices of the right face of the sub_part part of the chair
            sub_part_right = (b,f,g,c)
            sub_part.append(sub_part_right)

            # This vector stores the vertices of the left face of the sub_part part of the chair
            sub_part_left = (e,a,d,h)
            sub_part.append(sub_part_left)

            # This vector stores the vertices of the top face of the sub_part part of the chair
            sub_part_top = (c,g,h,d)
            sub_part.append(sub_part_top)

            # This vector stores the vertices of the bottom face of the sub_part part of the chair
            sub_part_bottom = (a,e,f,b)
            sub_part.append(sub_part_bottom)

            chair.append(sub_part)

        self.chairs.append(chair)

    def get_chairs(self):
            return self.chairs
