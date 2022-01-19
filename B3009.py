Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())

if (Ax == Bx):
    Dx = Cx
elif (Ax == Cx):
    Dx = Bx
elif (Bx == Cx):
    Dx = Ax

if (Ay == By):
    Dy = Cy
elif (Ay == Cy):
    Dy = By
elif (By == Cy):
    Dy = Ay

print(Dx, Dy)
