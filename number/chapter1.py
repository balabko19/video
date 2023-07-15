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
        
        label2 = axx.get_axis_labels(
            Tex('X').scale(0.45),
            Tex('Y').scale(0.45)
            )
        
        str1 = Text ('N - колличество еды\nМ - колличество килограмм', font_size=18).shift(UR *2 + RIGHT)
        str2 = Tex('$M = f(N)$').next_to(axx, UP)
        str3 = Text ('X - аргумент\nY - зависимая величина', font_size=18).shift(UR *2 + RIGHT)
        str4 = Tex('$Y = f(X)$').next_to(axx, UP)

        #dots = VGroup(*[Dot() for j in range(5)]).arrange(LEFT, buff = 1)
        line_graph= axx.plot_line_graph(
            x_values =[0,2,5],
            y_values =[0,1,2.5],
            line_color= RED
        )




        ####
        self.add(title, plane)
        self.play(Transform(title, axx), run_time= 3)
        self.wait(2)
        self.play( Create(label))
        self.wait(2)
        self.play(Create(str1))
        self.wait(2)
        self.play(Create(str2))
        self.wait(2)
        self.play(Create(line_graph))
        self.wait(2)
        self.play(Transform(str1,str3), Transform(label, label2), Transform(str2,str4 ))






    
