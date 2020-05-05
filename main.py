import json
from element import Metal, Nonmetal
import sys


with open('data.json', 'r') as f:
    data = json.load(f)


def sub_sup(formula, mode):  # mode SUB or SUB
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")  # subscript
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")  # superscript

    if mode == 'SUB':
        # can chanage .translate(VALUE), (SUB) or (SUP)
        return formula.translate(SUB)
    elif mode == 'SUP':
        return formula.translate(SUP)
    else:
        return 'Error must use SUB or SUP'


def main():

    while True:
        
        try:  # TODO  better input validation
            print('\n')  # readability
            metal, nonmetal = input('Enter {Metal Nonmetal}: ').split()

        except:  # user entered blank to end loop
            print('Invalid Input try again')
            sys.exit()

        try:
            if len(metal) > 2 and len(nonmetal) > 2:
                """[checks if user input long format ie: sodium chloride]
                """
                metal = Metal(metal.capitalize(), 'name')
                nonmetal = Nonmetal(nonmetal.capitalize(), 'suffix')

            else:
                metal = Metal(metal.capitalize(), 'symbol')
                nonmetal = Nonmetal(nonmetal.capitalize(), 'symbol')
                print(f"{metal.full_name} {nonmetal.compound}")
        except:
            print('Error input must be [metal nonmetal]')
            print('Support for Multivalent and Transition Metals coming soon')
            print('Exiting...')
            sys.exit()

        # if metal charge == nonmetal charge remove the subscript
        if abs(metal.charge) == abs(nonmetal.charge):
            output = f"{metal.symbol}{nonmetal.symbol}"

        elif abs(metal.charge) <= 1:  # if metal charge <= 1 then remove subscript for metal
            output = f"{metal.symbol}{abs(nonmetal.charge)}{nonmetal.symbol}"

        elif abs(nonmetal.charge) <= 1:  # if nonmetal charge <= 1 then remove subscript for nonmetal
            output = f"{metal.symbol}{nonmetal.symbol}{abs(metal.charge)}"

        else:
            output = f"{metal.symbol}{abs(nonmetal.charge)}{nonmetal.symbol}{abs(metal.charge)}"

        print(sub_sup(output, 'SUB'))


if __name__ == "__main__":
    main()
