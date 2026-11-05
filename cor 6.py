import cv2
import turtle
import sys

IMAGE = "spiderman.png"  # Rasim nomi shu papkada bo‘lishi kerak

img = cv2.imread(IMAGE)

if img is None:
    print("Image not found!")
    sys.exit()

# Resize
height = 700
ratio = height / img.shape[0]
width = int(img.shape[1] * ratio)
img = cv2.resize(img, (width, height))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold
_, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)

# Contours topish
contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_NONE
)

# Kichik shovqinlarni olib tashlash
contours = [c for c in contours if cv2.contourArea(c) > 15]

# Katta shakllardan boshlab chizish
contours = sorted(contours, key=cv2.contourArea, reverse=True)

# Turtle sozlash
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.tracer(0)  # Tezroq chizish uchun

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.color("black")
pen.hideturtle()

# Konturlarni chizish
for contour in contours:
    pen.penup()
    # Birinchi nuqtaga o‘tish
    start_x = contour[0][0][0] - width // 2
    start_y = height // 2 - contour[0][0][1]
    pen.goto(start_x, start_y)
    pen.pendown()

    for point in contour:
        x = point[0][0] - width // 2
        y = height // 2 - point[0][1]
        pen.goto(x, y)

screen.update()
turtle.done()