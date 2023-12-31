from PIL import Image, ImageDraw
from math import pi
from Fractal import Fractal

def printFractal(fractal, rule):
    while rule:
        c = rule[0]
        match c:
            case "F":
                fractal.F()
            case "+":
                fractal.positive()
            case "-":
                fractal.negative()
            case "[":
                f = fractal.__copy__()
                rule = printFractal(f, rule[1:])
            case "]":
                return rule
        rule = rule[1:]


def main():

    width, height = 1000, 1000
    image = Image.new("RGB", (width, height), "skyblue")
    draw = ImageDraw.Draw(image)
    color = (0,0,0)

    axioma = input("Input axioma: ")
    newRule = input("Input rule: ")
    n = int(input("Enter N: "))
    r = int(input("Enter R: "))
    alpha = float(input("Enter alpha: "))
    theta = float(input("Enter theta: "))
    len = int(input("Enter length: "))
    width = int(input("Enter width: "))
    x0 , y0 = int(input("Enter x0: ")), int(input("Enter y0: "))
    name = input("Input image name: ")
    
    fractal = Fractal(x0, y0, alpha, theta, len, width, draw, color)

    for _ in range(0, n):
        fractal.len /= r
        axioma = axioma.replace('F', newRule)
    
    printFractal(fractal, axioma)
    print("Result: ", axioma)

    image.save(f"{name}.png")
    image.show()

if __name__ == "__main__":
    main()