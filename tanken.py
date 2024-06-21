def tanken( kilometers_per_liter, tankinhoud, te_rijden_afstand):
    tankbeurten = 0
    while te_rijden_afstand > 0:
        test = tankinhoud * kilometers_per_liter
        te_rijden_afstand -= test

        tankbeurten += 1
    return tankbeurten

verwachteresults = [2, 1, 2, 3, 4, 2, 2, 1, 3, 1]

test1 = tanken(2, 10, 40) == verwachteresults[0]
test2 = tanken(1, 40, 40) == verwachteresults[1]
test3 = tanken(3, 15, 60) == verwachteresults[2]
test4 = tanken(1, 30, 90) == verwachteresults[3]
test5 = tanken(3, 10, 120) == verwachteresults[4]
test6 = tanken(100, 1, 200) == verwachteresults[5]
test7 = tanken(50, 10, 524) == verwachteresults[6]
test8 = tanken(24, 20, 63) == verwachteresults[7]
test9 = tanken(3, 12, 83) == verwachteresults[8]
test10 = tanken(7, 28, 57) == verwachteresults[9]



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