def get_line(x0, y0, x1, y1):
    dx, dy = x1 - x0, y1 - y0
    #primera iteracion, punto inicial pertenece a la recta
    xk = x0
    yk = y0
    points = [(x0, y0)]
    Pk = 2 * dy - dx

    while xk != x1:
        if x0 < x1:
            xk += 1
            if Pk > 0:
                yk += 1
                Pk = Pk + 2 * dy - 2 * dx
            else:
                Pk = Pk + 2 * dy
        else:
            xk -= 1
            if Pk < 0:
                yk -= 1
                Pk = Pk + 2 * dy - 2 * dx
            else:
                Pk = Pk + 2 * dy
        points.append((xk, yk))
    return points
#print(get_line(6,2,1,0))