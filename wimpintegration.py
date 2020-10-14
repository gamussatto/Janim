from manimlib.imports import *
from math import sqrt, tan, cos, sin, pi

class Physics(GraphScene):
    CONFIG = {
        "function_color": PINK,
        "axes_color": BLUE,
        "x_labeled_nums": range(0,12,2),
        "y_labeled_nums": range(0,6,2),
        "x_axis_label": "$t/s$",
        "y_axis_label": "$a/ms^{-2}$",
    }

    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label="0.4x")
        areaEquation = TextMobject("$$1/2(4*10) = 20ms$$")
        areaEquation.set_color_by_gradient("#33ccff","#ff00ff")

        # Visualizing the calculation of the area
        x = self.coords_to_point(10, self.func_to_graph(10))
        y = self.coords_to_point(0, self.func_to_graph(0))
        yn = self.coords_to_point(0, self.func_to_graph(10))

        vert_line = self.get_vertical_line_to_graph(10, func_graph, color=YELLOW)
        horz_line = Line(x,y, color=YELLOW)
        horz_line_normal = Line(x,yn, color=YELLOW)

        point =  Dot(self.coords_to_point(10, self.func_to_graph(10)))
        integral_triangle_up = Polygon(x,y,yn, fill_color=BLUE, fill_opacity=1)
        # --

        # -- Composition Scene 1 --
        self.play(ShowCreation(func_graph), Write(graph_lab))
        self.wait(0.5)
        self.play(ShowCreation(vert_line))
        self.play(ShowCreation(horz_line))
        self.add_foreground_mobject(point)
        self.wait(1)
        self.play(ShowCreation(horz_line_normal), Write(areaEquation))
        self.play(FadeIn(integral_triangle_up))
        self.wait(1)
        self.x_axis_label = "$t/s$"
        self.y_axis_label = "$v/ms^{-1}$"
        self.y_min = -2
        self.y_max = 2
        self.x_min = 0
        self.x_max = 8
        self.y_labeled_nums = range(-3,3,1)
        self.x_labeled_nums = range(0,9,1)
        self.graph_origin = 0 * DOWN + 4 * LEFT,
        self.play(FadeOutAndShiftDown(vert_line), FadeOutAndShiftDown(horz_line), FadeOutAndShiftDown(point),
                  FadeOutAndShiftDown(func_graph), FadeOutAndShiftDown(graph_lab), FadeOutAndShiftDown(horz_line_normal))
        self.wait(1)
        self.play(FadeOut(integral_triangle_up), FadeOut(areaEquation), FadeOut(self.axes))
        self.wait(2)
        # -- Composition Scene 1--

        # -- Composition Scene 2 --
        eq1 = TextMobject("$v(t) = u + at$")
        eq2 = TextMobject("$$\\int_{a}^{b} v(t) \\,dt$$")
        eq3 = TextMobject("$$\\int_{3}^{6} 2+9.81t \\,dt$$")
        eq4 = ["$$[\\frac{9.81(6)^2}{2} + 2(6)] - [\\frac{9.81(3)^2}{2} + 2(3)]$$", "$ = $", "$138.4m$"]
        eq4 = TextMobject(*eq4)
        for i, item in enumerate(eq4):
            if i != 0:
                item.next_to(eq4[i-1], RIGHT)
        eq4 = VGroup(*eq4)

        eq1.shift(2*UP)
        eq4.shift(LEFT)
        eq2.set_color_by_gradient("#33ccff","#ff00ff")
        eq3.set_color_by_gradient("#33ccff","#ff00ff")
        eq4.set_color_by_gradient("#33ccff","#ff00ff")

        self.play(Write(eq1), Write(eq2))
        self.wait(2)
        self.play(ReplacementTransform(eq2, eq3))
        self.wait(2)
        self.play(Transform(eq3, eq4[0]))
        self.play(Write(eq4[1]), Write(eq4[-1]))
        self.wait(2)
        # -- Composition Scene 2 --

    def func_to_graph(self, x):
        return(0.4*x)

    def func_to_graph_2(self, x):
        return(sin(x))

    def recursive_integration(self, x, n):
        # Not functional at the moment
        width = (x[-1] - x[0])/n
        sample = np.array([])

        for i in range(n):
            height = self.func_to_graph((n+1)*width)
            if i != 0:
                sample = np.append(sample, Rectangle(height=height,
                                                     width=width,
                                                     fill_color=BLUE,
                                                     fill_opacity=1,
                                                     color=PINK).next_to(sample[i-1],
                                                                         RIGHT))
            sample = np.append(sample, Rectangle(height=height, width=width,
                                                 fill_color=BLUE,
                                                 fill_opacity=1,
                                                 color=PINK).shift(x[0]+3.4*LEFT).shift(0.4*DOWN))
        return sample
