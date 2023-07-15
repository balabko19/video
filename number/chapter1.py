from manim import*

class whatfunction(Scene):
    def construct(self):
        plane = NumberPlane()

        title = Text('Что такое функция f(x)?').shift(UP * 3)
        axx = Axes(
            x_range=[0, 5],
            y_range=[0, 5],
            tips= True,
            axis_config={"color": GOLD_A}
        ).scale(0.5).shift(DL + LEFT)

        label = axx.get_axis_labels(
            Tex('N').scale(0.45),
            Tex('M').scale(0.45)
            )
        
        str1 = Text ('N - колличество еды\nМ - колличество килограмм', font_size=18).shift(UR *2 + RIGHT)
        str1[0].set_color(RED) ###ПЕРЕДЕЛАТЬ
        str1[16].set_color(RED)

        dots = VGroup(*[Dot() for j in range(5)]).arrange(np.around(axx.coords_to_point(0, 0, 0), 0), buff= 0.01)




        ####
        self.add(title, plane)
        self.play(Transform(title, axx), run_time= 3)
        self.wait(2)
        self.play( Create(label))
        self.wait(2)
        self.play(Create(str1))
        self.wait(2)
        self.play(Create(dots))
        self.wait(2)
        ####
        



    
