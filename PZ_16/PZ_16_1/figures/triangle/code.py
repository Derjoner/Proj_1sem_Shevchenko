def triangle_perimeter(a=7, b=2, c=8):
    """Вычисление периметра треугольника

        Принимает стороны: а, b, c

    """
    return a+b+c

def triangle_area(a=7, b=2, c=8):
    """Вычисление площади треугольника

        Принимает стороны: а, b, c

    """
    p = triangle_perimeter(a, b, c)/2
    return (p*(p-a)*(p-b)*(p-c))**(0.5)