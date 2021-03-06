import math

class Front:


    def __init__(self):
        self.reference = (0, 0, 0) #x, y and z of the floor
        #A for iteration for each one of the seven parts that compose the front
        n_parts = 150
        self.sub_part_half_width = [3.125, 3.125, 0.75, 7, 7]
        self.sub_part_half_height = [2, 2, 0.624, 1.5, 1.5]
        self.sub_part_half_depth = [0.1, 0.1, 0.1, 0.1, 0.1]
        w, h, d = self.__get_arc_dims(n_parts)
        self.sub_part_half_width.extend(w)
        self.sub_part_half_height.extend(h)
        self.sub_part_half_depth.extend(d)
        self.sub_part_center = self.__get_sub_part_center(self.reference, w, h)
        self.front = []

        self.__generate_coordinates()

    def __get_arc_dims(self, n_parts):
        door_width  = 1.5
        door_begin  = -0.75
        wall_depth  = 0.2
        r           = 0.75

        rect_half_width = (door_width/n_parts)/2
        half_widths     = [rect_half_width]*n_parts

        rect_half_depth = (wall_depth)/2
        half_depths     = [rect_half_depth]*n_parts

        x = door_begin + rect_half_width
        half_heights    = []
        for i in range(n_parts):
            h = math.sqrt(math.pow(r, 2) - math.pow(x, 2))
            half_heights.append((r - h)/2)

            x += half_widths[0]*2

        return half_widths, half_heights, half_depths

    def __get_arc_centers(self, reference, half_widths, half_heights):
        centers = []
        z_centers = 19.88
        x_i = -0.75
        y_i = 2.75

        for w, h in zip(half_widths, half_heights):
            center = (reference[0] + x_i + w, reference[1] + y_i - h,
                        reference[2] + z_centers)
            x_i += 2*w

            centers.append(center)

        return centers

    def __get_sub_part_center(self, reference, w, h):

        sub_part_center = [
                        (reference[0] - 3.875, reference[1] + 1.9, reference[2] + 19.88),
                        (reference[0] + 3.875, reference[1] + 1.9, reference[2] + 19.88),
                        (reference[0] + 0, reference[1] + 3.375, reference[2] + 19.88),
                        (reference[0] + 0, reference[1] + 5.5, reference[2] + 19.88),
                        (reference[0] + 0, reference[1] + 8.5, reference[2] + 19.88)
                        ]

        sub_part_center.extend(self.__get_arc_centers(reference, w, h))
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

        # For loop to generate all the coordinates of the front parts
        print(len(self.sub_part_half_height))
        for i in range(len(self.sub_part_half_height)):
            sub_part = []

            a, b, c, d, e, f, g, h = self.__gen_vertexes(i)

            # This vector stores the vertices of the front face of the sub_part part of the front
            sub_part_front = (a,b,c,d)
            sub_part.append(sub_part_front)

            # This vector stores the vertices of the sub_part face of the sub_part part of the front
            sub_part_back = (e,f,g,h)
            sub_part.append(sub_part_back)

            # This vector stores the vertices of the right face of the sub_part part of the front
            sub_part_right = (b,f,g,c)
            sub_part.append(sub_part_right)

            # This vector stores the vertices of the left face of the sub_part part of the front
            sub_part_left = (e,a,d,h)
            sub_part.append(sub_part_left)

            # This vector stores the vertices of the top face of the sub_part part of the front
            sub_part_top = (c,g,h,d)
            sub_part.append(sub_part_top)

            # This vector stores the vertices of the bottom face of the sub_part part of the front
            sub_part_bottom = (a,e,f,b)
            sub_part.append(sub_part_bottom)

            self.front.append(sub_part)

    def get_front(self):
        return self.front
