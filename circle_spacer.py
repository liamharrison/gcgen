import gcgen

result = gcgen.generic_setup(2)
result += gcgen.helicut_circle(0, 0, 1.8, -6, 2, 400, 4)
result += gcgen.helicut_circle(0, 0, 11.8, -6, 2, 400, 4)

print(result)