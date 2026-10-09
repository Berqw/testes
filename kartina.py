import turtle
import random
import math

screen = turtle.Screen()
screen.setup(900, 700)
screen.bgcolor("skyblue")
screen.tracer(0)  # рисуем мгновенно, обновим экран в конце

t = turtle.Turtle()
t.hideturtle()
t.speed(0)


# ================= базовые функции =================
def go(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()


def rect(x, y, w, h, color):
    go(x, y)
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()


def circle(x, y, r, color):
    go(x, y - r)
    t.color(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()


def poly(points, color):
    go(*points[0])
    t.color(color)
    t.begin_fill()
    for p in points[1:]:
        t.goto(p)
    t.goto(points[0])
    t.end_fill()


def line(x1, y1, x2, y2, color, width=1):
    go(x1, y1)
    t.color(color)
    t.pensize(width)
    t.goto(x2, y2)
    t.pensize(1)


def cloud(x, y):
    circle(x, y, 25, "white")
    circle(x + 25, y + 12, 30, "white")
    circle(x + 55, y, 25, "white")
    circle(x + 25, y - 8, 25, "white")


def bird(x, y):
    t.color("black")
    t.pensize(2)
    go(x - 12, y + 6)
    t.goto(x, y)
    t.goto(x + 12, y + 6)
    t.pensize(1)


def flower(x, y, color):
    line(x, y, x, y + 20, "darkgreen", 2)
    for a in range(0, 360, 72):
        px = x + 7 * math.cos(math.radians(a))
        py = y + 20 + 7 * math.sin(math.radians(a))
        circle(px, py, 5, color)
    circle(x, y + 20, 4, "yellow")


# ================= машина Honda Accord 8 =================
def car(ox, oy, s=1.0, body="#1c3b7a"):
    def P(x, y):
        return (ox + x * s, oy + y * s)

    def cpoly(pts, color):
        poly([P(*p) for p in pts], color)

    def cline(a, b, color, w=1):
        line(*P(*a), *P(*b), color, w * s)

    def ccircle(x, y, r, color):
        circle(*P(x, y), r * s, color)

    def wheel(cx, cy):
        ccircle(cx, cy, 21, "black")        # арка
        ccircle(cx, cy, 19, "#111111")      # шина
        ccircle(cx, cy, 13, "silver")       # обод
        ccircle(cx, cy, 10, "#333333")
        ccircle(cx, cy, 6, "firebrick")     # тормозной суппорт
        for a in range(0, 360, 72):         # спицы
            cline((cx, cy),
                  (cx + 11 * math.cos(math.radians(a + 18)),
                   cy + 11 * math.sin(math.radians(a + 18))),
                  "silver", 3.5)
        ccircle(cx, cy, 4, "silver")
        ccircle(cx, cy, 1.5, "gold")

    # тень
    cpoly([(-8, -3), (275, -3), (275, 1), (-8, 1)], "darkgreen")

    # кузов
    cpoly([(2, 14), (0, 36), (7, 48), (66, 52), (97, 72), (160, 74),
           (192, 52), (236, 46), (256, 40), (264, 28), (262, 14)], body)

    # стёкла (тонировка) и блик
    cpoly([(72, 54), (98, 69), (158, 71), (186, 54)], "#26323f")
    cline((108, 68), (124, 56), "#4a5f78", 3)
    cline((140, 69), (152, 57), "#4a5f78", 3)
    cline((128, 54), (128, 71), body, 5)    # стойка B

    # линии дверей, ручки, молдинг
    for x in (72, 128, 186):
        cline((x, 52), (x, 18), "#0a1633", 1.2)
    cpoly([(105, 46), (119, 46), (119, 43), (105, 43)], "silver")
    cpoly([(150, 46), (164, 46), (164, 43), (150, 43)], "silver")
    cline((8, 38), (255, 33), "#13285a", 1.5)

    # зеркало
    cpoly([(184, 56), (198, 54), (197, 60), (186, 61)], body)

    # фары
    cpoly([(236, 46), (256, 40), (260, 32), (242, 34)], "lightyellow")
    cpoly([(244, 42), (255, 38), (257, 34), (246, 36)], "gold")
    cpoly([(0, 36), (2, 44), (8, 47), (12, 44), (10, 36)], "red")

    # ОБВЕС: передняя губа и воздухозаборник
    cpoly([(246, 16), (262, 16), (260, 26), (247, 26)], "black")
    ccircle(253, 21, 3, "lightyellow")      # противотуманка
    cpoly([(236, 8), (272, 8), (264, 16), (236, 16)], "black")
    cline((238, 10), (270, 10), "red", 1.5)

    # ОБВЕС: пороги с красной полосой
    cpoly([(76, 9), (188, 9), (184, 19), (80, 19)], "black")
    cline((78, 12), (186, 12), "red", 1.5)

    # ОБВЕС: задний диффузор и выхлоп
    cpoly([(-3, 8), (42, 8), (48, 16), (-3, 16)], "black")
    cline((-3, 10), (40, 10), "red", 1.5)
    cpoly([(-8, 9), (1, 9), (1, 14), (-8, 14)], "silver")
    cpoly([(-8, 3), (1, 3), (1, 8), (-8, 8)], "silver")

    # ОБВЕС: спойлер
    cpoly([(14, 49), (18, 49), (18, 63), (14, 63)], "black")
    cpoly([(38, 50), (42, 50), (42, 63), (38, 63)], "black")
    cpoly([(2, 63), (56, 63), (56, 68), (2, 68)], "black")
    cline((2, 68), (56, 68), "red", 1)

    # колёса
    wheel(52, 19)
    wheel(210, 19)


# ================= небо =================
# солнце с лучами
circle(-300, 200, 45, "yellow")
for a in range(0, 360, 30):
    go(-300, 200)
    t.setheading(a)
    t.penup()
    t.forward(55)
    t.pendown()
    t.color("orange")
    t.pensize(3)
    t.forward(25)
t.pensize(1)

# облака и птицы
cloud(-120, 220)
cloud(120, 190)
cloud(280, 240)
bird(-40, 130)
bird(10, 160)
bird(60, 125)

# ================= горы =================
poly([(-400, -100), (-250, 100), (-100, -100)], "slategray")
poly([(-295, 40), (-250, 100), (-205, 40), (-230, 50), (-250, 35), (-270, 50)], "white")
poly([(-200, -100), (-30, 150), (140, -100)], "gray")
poly([(-78, 80), (-30, 150), (18, 80), (0, 95), (-30, 75), (-55, 95)], "white")
poly([(50, -100), (250, 60), (400, -100)], "slategray")

# ================= земля =================
rect(-400, -300, 800, 200, "forestgreen")
poly([(-20, -170), (20, -170), (60, -300), (-60, -300)], "tan")  # дорожка

# ================= забор =================
line(-390, -165, -130, -165, "white", 5)
line(-390, -185, -130, -185, "white", 5)
for x in range(-390, -130, 30):
    rect(x, -200, 10, 50, "white")

# ================= дом =================
rect(-100, -170, 200, 140, "orange")
rect(55, -10, 25, 70, "firebrick")                   # труба
poly([(-120, -30), (0, 60), (120, -30)], "darkred")  # крыша
# дым
circle(68, 75, 8, "lightgray")
circle(78, 95, 11, "lightgray")
circle(92, 118, 14, "lightgray")
# дверь
rect(-20, -170, 40, 80, "saddlebrown")
circle(10, -130, 3, "gold")
# окна
for wx in (-85, 40):
    rect(wx, -120, 45, 45, "lightyellow")
    line(wx + 22.5, -120, wx + 22.5, -75, "black", 2)
    line(wx, -97.5, wx + 45, -97.5, "black", 2)
# круглое окошко на крыше
circle(0, 15, 14, "lightyellow")
line(-14, 15, 14, 15, "black", 2)
line(0, 1, 0, 29, "black", 2)

# ================= яблоня =================
rect(240, -200, 24, 100, "saddlebrown")
circle(252, -60, 55, "darkgreen")
circle(222, -80, 40, "darkgreen")
circle(282, -80, 40, "darkgreen")
for ax, ay in [(235, -50), (270, -70), (215, -85), (255, -30), (290, -95)]:
    circle(ax, ay, 6, "red")

# ================= цветы =================
random.seed(5)
colors = ["red", "pink", "white", "violet", "orange"]
for _ in range(16):
    fx = random.randint(-380, 380)
    fy = random.randint(-290, -215)
    if abs(fx) > 70:
        flower(fx, fy, random.choice(colors))

# ================= машина =================
car(-395, -275, 0.9)   # цвет можно сменить: car(-395, -275, 0.9, "red")

screen.update()
turtle.done()
