import gcgen

result = gcgen.generic_setup(2)
result += gcgen.helicut_circle(10, 10, 1.8, -6, 2, 400, 4)
result += gcgen.helicut_circle(10, 140, 1.8, -6, 2, 400, 4)
result += gcgen.helicut_circle(90, 140, 1.8, -6, 2, 400, 4)
result += gcgen.helicut_circle(90, 10, 1.8, -6, 2, 400, 4)

result += gcgen.helicut_circle(37.5, 20, 1.8, -6, 2, 400, 4)
result += gcgen.helicut_circle(62.5, 20, 1.8, -6, 2, 400, 4)
result += gcgen.helicut_circle(37.5, 72.5, 1.8, -6, 2, 400, 4)
result += gcgen.helicut_circle(62.5, 72.5, 1.8, -6, 2, 400, 4)

result += gcgen.rectangle_outside(0, 0, 100, 150, 1000, 50, 3.2, 2, [-6])

print(result)