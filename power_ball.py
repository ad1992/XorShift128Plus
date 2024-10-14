# Print 'last seen' random number
#   and winning numbers following that.
# This was for debugging. We know that Math.random()
#   is called in the browser zero times (updated) for each page click 
#   in Chrome and once for each page click in Firefox.
#   Since we have to click once to enter the numbers
#   and once for Play, we indicate the winning numbers
#   with an arrow.
def power_ball(generated, browser):
    # for each random number (skip 4 of 5 that we generated)
    for idx in range(len(generated[4:])):
        # powerball range is 1 to 69
        poss = list(range(1, 70))
        # base index 4 to skip
        gen = generated[4+idx:]
        # get 'last seen' number
        g0 = gen[0]
        gen = gen[1:]
        # make sure we have enough numbers 
        if len(gen) < 6:
            break
        print(g0)

        # generate 5 winning numbers
        nums = []
        for jdx in range(5):
            index = int(gen[jdx] * len(poss))
            val = poss[index]
            poss = poss[:index] + poss[index+1:]
            nums.append(val)

        # print indicator
        if idx == 0 and browser == 'chrome':
            print('--->', end='')
        elif idx == 2 and browser == 'firefox':
            print('--->', end='')
        else:
            print('    ', end='')
        # print winning numbers
        print(sorted(nums), end='')

        # generate / print power number or w/e it's called
        double = gen[5]
        val = int(math.floor(double * 26) + 1)
        print(val)
