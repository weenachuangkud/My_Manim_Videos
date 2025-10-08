# author: Mawin CK
# date  : 2025-06-20
# description: Basic Arithmetic Operations using Manim

#I'm still learning how to code and using Manim 
#Expect some issues and bad code :P

from random import randint
from random import choice
from manim import *

class BasicArithmetic(Scene):
    timeLatex = r"\times"

    def fracLatex(self, a: int, b: int) -> str:
        return rf"\frac{{{a}}}{{{b}}}"

    def do_Operation(self, a: int, operator: str, b: int) -> str:
        try:
            result = eval(f"{a} {operator} {b}")
            match operator:
                case "*":
                    return f"{a} {self.timeLatex} {b} = {result}"
                case "/":
                    return f"{self.fracLatex(a, b)} = {result}"
                case _:
                    return f"{a} {operator} {b} = {result}"
        except Exception as e:
            return f"Error: {e}"

    def construct(self):
        operationStr  = ['+', '-', '*', '/']
        operations = [
            (5, '+', 3),
            (10, '-', 4),
            (6, '*', 7),
            (20, '/', 5),
            *[(randint(100, 10000), choice(operationStr), randint(100, 10000)) for i in range(12)]
        ]
        exprs = [MathTex(self.do_Operation(a, op, b)).scale(1.5) for a, op, b in operations]

        self.introduction(1)
        self.play(Write(exprs[0]), run_time=1)
        self.play(exprs[0].animate.set_color(RED), run_time=1.2)
        self.play(exprs[0].animate.set_color(WHITE), run_time=0.5)

        self.SeqOperations(exprs, 0.5, 1)
        
        conclusion = Text("Conclusion : Order of Operations are not same", font_size=32)
        self.play(Write(conclusion), run_time=0.5)
        self.play(conclusion.animate.set_color(YELLOW), run_time=1)
        
        self.play(Transform(conclusion, Text("Let's see with Multiplication and Division", font_size=32)), run_time=1)
        self.play(FadeOut(conclusion), run_time=0.5)

        self.DifferenceOrderOperations(3, "*", 4, 1, 0.5)
        self.DifferenceOrderOperations(12, "/", 4, 1, 0.5)
        
        operations = [
            *[(randint(100000, 100000000), choice(operationStr), randint(1000000, 100000000)) for i in range(30)],
        ]
        exprs = [MathTex(self.do_Operation(a, op, b)).scale(1.5) for a, op, b in operations]
        self.wait(1)
        self.SeqOperations(exprs, 0.6, 2)

    def SeqOperations(self, exprs : list[MathTex], speed : int | float, fadeOutSec : int | float) -> None:
        for i in range(len(exprs) - 1):
            exprs[i + 1].move_to(exprs[i].get_center())
            self.play(Transform(exprs[i], exprs[i + 1]), run_time=speed)
            self.remove(exprs[i])
        self.play(FadeOut(exprs[-1], run_time=fadeOutSec))
        
    def introduction(self, fadeOutSpeed : int|float) -> None:
        title = Text("Basic Arithmetic Operations", font_size=48)
        subtitle = Text("Animated Using Manim", font_size=36).next_to(title, DOWN)
        self.play(Write(title))
        self.play(Write(subtitle), run_time=1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=fadeOutSpeed)
        
    def DifferenceOrderOperations(self, a: int, operation: str, b: int, anim_speed: int | float, fadeoutSpeed: int | float) -> None:
        if operation not in ["*", "/"]:
            raise ValueError("Operation must be either multiplication or division")
        
        diff = MathTex(self.do_Operation(a, operation, b)).scale(1.5)

        position_label = Text("Position").scale(1).to_edge(UP).set_color(RED)
        
        self.play(Write(position_label), Write(diff), run_time=anim_speed)
        self.wait(anim_speed)

        expr = self.fracLatex(b, a) if operation == "/" else rf"{b} {self.timeLatex} {a}"

        swapped_expr = MathTex(expr, r"\neq", str(eval(f'{a} {operation} {b}'))).scale(1.5)
        swapped_expr.move_to(diff.get_center())

        self.play(Transform(diff, swapped_expr), run_time=anim_speed)
        self.play(FadeOut(diff), FadeOut(position_label), run_time=fadeoutSpeed)
