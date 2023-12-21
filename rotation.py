from manim import *
import numpy as np

class Rotation(MovingCameraScene):
    def construct(self):
        x=float(input("Введите координату вектора по оси абсцисс: "))
        y=float(input("Введите координату вектора по оси ординат: "))
        angle=float(input("Введите угол поворота в градусах (положительный угол отвечает за поворот против часовой стрелки): "))
        xaxes = (abs(x)*2+1)//2+1
        yaxes = (abs(y)*2+1)//2+1
        radians=angle*np.pi/180
        axes = Axes(
            x_range=[-10,10,1],
            y_range=[-10,10,1],
            x_length=6.6,
            y_length=6.6,
            axis_config={'color':GREEN},
            x_axis_config={
                           'numbers_with_elongated_ticks': np.arange(-10,10+0.01,10),
                           'numbers_to_include': np.arange(-10,10+0.01,10)},
            y_axis_config = {
                         'numbers_with_elongated_ticks': np.arange(-10, 10+0.01, 10),
                         'numbers_to_include': np.arange(-10, 10+0.01, 10)}
        )
        axes_labels = axes.get_axis_labels()
        vector=Vector(np.array([x/3,y/3]), color=BLUE)
        vector.set_stroke(width=3)
        rotation_matrix = np.array([
            [np.cos(radians), -np.sin(radians)],
            [np.sin(radians), np.cos(radians)]
        ])
        rotated_vector = np.array([rotation_matrix[0][0]*x/3+rotation_matrix[0][1]*y/3,rotation_matrix[1][0]*x/3+rotation_matrix[1][1]*y/3])
        matrix = MathTex(
            r"R = \begin{bmatrix} \cos(\phi) & \sin(\phi) \\ -\sin(\phi) & \cos(\phi) \end{bmatrix}"
        )
        phi = MathTex(r"\phi =")
        phi.move_to(UP*1.5+LEFT*6.2)
        text_angle = Text(f"{angle} degrees",font_size=24)
        text_angle.move_to(UP*1.5+LEFT*4.7)
        matrix.set_height(0.7)
        matrix.move_to(UP*3.3+LEFT*5.2)
        self.play(Write(matrix))
        self.play(Write(phi))
        self.play(Create(text_angle))
        x1=round(np.cos(radians)*x-np.sin(radians)*y,3)
        y1=round(np.sin(radians)*x+np.cos(radians)*y,3)
        self.wait()
        plots=VGroup(axes,vector)
        labels=VGroup(axes_labels)
        rot_vector=Vector(rotated_vector, color=RED, stroke_width=3)
        text1 = Text(f"({x}, {y})", font_size=24, color=BLUE)
        text1.next_to(vector, direction=RIGHT)
        text2 = Text(f"({x1},{y1})", font_size=24,color=RED)
        text2.next_to(rot_vector,direction=RIGHT)
        self.play(Create(plots), Create(text1), run_time=6)
        self.play(Create(labels),run_time=2)
        self.play(Transform(vector,rot_vector,run_time=2),Transform(text1,text2,run_time=2))
        self.wait(3)