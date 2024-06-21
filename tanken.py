def tanken( kilometers_per_liter, tankinhoud, te_rijden_afstand):
    tankbeurten = 0
    while True:
        test = tankinhoud * kilometers_per_liter
        te_rijden_afstand -= test
        
        tankbeurten += 1
        if te_rijden_afstand <= 0:
            break
    return tankbeurten

test1 = tanken(2, 10, 40)
test2 = tanken(1, 40, 40)
test3 = tanken(3, 15, 60)
test4 = tanken(1, 30, 90)
test5 = tanken(3, 10, 120)
test6 = tanken(100, 1, 200)
test7 = tanken(50, 10, 524)
test8 = tanken(24, 20, 63)
test9 = tanken(3, 12, 83)
test10 = tanken(7, 28, 57)


print(test1,
      test2,
      test3,
      test4,
      test5,
      test6,
      test7,
      test8,
      test9,
      test10)