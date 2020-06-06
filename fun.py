# noinspection SpellCheckingInspection
def punnet(parent1, parent2, n, display):
    import itertools

    n1 = len(parent1)
    n2 = len(parent2)  # n2 = n1?
    alelos1 = [(parent1[i:i + n]) for i in range(0, n1, n)]
    alelos2 = [(parent2[i:i + n]) for i in range(0, n2, n)]

    combi1 = alelos1[0]
    combi2 = alelos2[0]
    for i in range(int(n1 / 2 - 1)):
        combi1 = [a + b for a, b in itertools.product(combi1, alelos1[i + 1])]
    for i in range(int(n2 / 2 - 1)):
        combi2 = [a + b for a, b in itertools.product(combi2, alelos2[i + 1])]

    table = []
    for e1 in combi1:
        row = []
        for e2 in combi2:
            # https://stackoverflow.com/questions/48403767/merge-two-strings-with-alternate-chars-as-output
            # e1_e2 = ''.join(map(''.join, zip(e1, e2))) # Does not care about upper/lower case order

            e1_e2 = ''.join((l1 + l2 if l1.isupper() else l2 + l1) for [l1, l2] in zip(e1, e2))

            row.append(e1_e2)
        table.append(row)

    if display:
        print('Combinations for table')
        print('Parent 1')
        print(list(combi1))
        print('Parent 2')
        print(list(combi2))
        for row in table:
            print(row)

    return table, combi1, combi2


def gens_with_colors(flower):
    genetic = {'Rose':  {'0000': 'White',   '0001': 'White',  '0002': 'White',
                   '0010': 'White',   '0011': 'White',  '0012': 'White',
                   '0020': 'Purple',  '0021': 'Purple', '0022': 'Purple',
                   '0100': 'Yellow',  '0101': 'Yellow', '0102': 'Yellow',
                   '0110': 'White',   '0111': 'White',  '0112': 'White',
                   '0120': 'Purple',  '0121': 'Purple', '0122': 'Purple',
                   '0200': 'Yellow',  '0201': 'Yellow', '0202': 'Yellow',
                   '0210': 'Yellow',  '0211': 'Yellow', '0212': 'Yellow',
                   '0220': 'White',   '0221': 'White',  '0222': 'White',
                   '1000': 'Red',     '1001': 'Pink',   '1002': 'White',
                   '1010': 'Red',     '1011': 'Pink',   '1012': 'White',
                   '1020': 'Red',     '1021': 'Pink',   '1022': 'Purple',
                   '1100': 'Orange',  '1101': 'Yellow', '1102': 'Yellow',
                   '1110': 'Red',     '1111': 'Pink',   '1112': 'White',
                   '1120': 'Red',     '1121': 'Pink',   '1122': 'Purple',
                   '1200': 'Orange',  '1201': 'Yellow', '1202': 'Yellow',
                   '1210': 'Orange',  '1211': 'Yellow', '1212': 'Yellow',
                   '1220': 'Red',     '1221': 'Pink',   '1222': 'White',
                   '2000': 'Black',   '2001': 'Red',    '2002': 'Pink',
                   '2010': 'Black',   '2011': 'Red',    '2012': 'Pink',
                   '2020': 'Black',   '2021': 'Red',    '2022': 'Pink',
                   '2100': 'Orange', '2101': 'Orange', '2102': 'Yellow',
                   '2110': 'Red',    '2111': 'Red',    '2112': 'White',
                   '2120': 'Black',  '2121': 'Red',    '2122': 'Purple',
                   '2200': 'Orange', '2201': 'Orange', '2202': 'Yellow',
                   '2210': 'Orange', '2211': 'Orange', '2212': 'Yellow',
                   '2220': 'Blue',   '2221': 'Red',    '2222': 'White',
                   },
               'Tulip': {'000': 'White',
                   '001': 'White',
                   '002': 'White',
                   '010': 'Yellow',
                   '011': 'Yellow',
                   '012': 'White',
                   '020': 'Yellow',
                   '021': 'Yellow',
                   '022': 'Yellow',
                   '100': 'Red',
                   '101': 'Pink',
                   '102': 'White',
                   '110': 'Orange',
                   '111': 'Yellow',
                   '112': 'Yellow',
                   '120': 'Orange',
                   '121': 'Yellow',
                   '122': 'Yellow',
                   '200': 'Black',
                   '201': 'Red',
                   '202': 'Red',
                   '210': 'Black',
                   '211': 'Red',
                   '212': 'Red',
                   '220': 'Purple',
                   '221': 'Purple',
                   '222': 'Purple',
                   },
               'Pansy': {'000': 'White',
                   '001': 'White',
                   '002': 'Blue',
                   '010': 'Yellow',
                   '011': 'Yellow',
                   '012': 'Blue',
                   '020': 'Yellow',
                   '021': 'Yellow',
                   '022': 'Yellow',
                   '100': 'Red',
                   '101': 'Red',
                   '102': 'Blue',
                   '110': 'Orange',
                   '111': 'Orange',
                   '112': 'Orange',
                   '120': 'Yellow',
                   '121': 'Yellow',
                   '122': 'Yellow',
                   '200': 'Red',
                   '201': 'Red',
                   '202': 'Purple',
                   '210': 'Red',
                   '211': 'Red',
                   '212': 'Purple',
                   '220': 'Orange',
                   '221': 'Orange',
                   '222': 'Purple',
                   },
               'Cosmos':{'000': 'White',
                   '001': 'White',
                   '002': 'White',
                   '010': 'Yellow',
                   '011': 'Yellow',
                   '012': 'White',
                   '020': 'Yellow',
                   '021': 'Yellow',
                   '022': 'Yellow',
                   '100': 'Pink',
                   '101': 'Pink',
                   '102': 'Pink',
                   '110': 'Orange',
                   '111': 'Orange',
                   '112': 'Pink',
                   '120': 'Orange',
                   '121': 'Orange',
                   '122': 'Orange',
                   '200': 'Red',
                   '201': 'Red',
                   '202': 'Red',
                   '210': 'Orange',
                   '211': 'Orange',
                   '212': 'Red',
                   '220': 'Black',
                   '221': 'Black',
                   '222': 'Red',
                   },
               'Lily':{'000': 'White',
                   '001': 'White',
                   '002': 'White',
                   '010': 'Yellow',
                   '011': 'White',
                   '012': 'White',
                   '020': 'Yellow',
                   '021': 'Yellow',
                   '022': 'White',
                   '100': 'Red',
                   '101': 'Pink',
                   '102': 'White',
                   '110': 'Orange',
                   '111': 'Yellow',
                   '112': 'Yellow',
                   '120': 'Orange',
                   '121': 'Yellow',
                   '122': 'Yellow',
                   '200': 'Black',
                   '201': 'Red',
                   '202': 'Pink',
                   '210': 'Black',
                   '211': 'Red',
                   '212': 'Pink',
                   '220': 'Orange',
                   '221': 'Orange',
                   '222': 'White',
                   },
               'Hyacinth':{'000': 'White',
                   '001': 'White',
                   '002': 'Blue',
                   '010': 'Yellow',
                   '011': 'Yellow',
                   '012': 'White',
                   '020': 'Yellow',
                   '021': 'Yellow',
                   '022': 'Yellow',
                   '100': 'Red',
                   '101': 'Pink',
                   '102': 'White',
                   '110': 'Orange',
                   '111': 'Yellow',
                   '112': 'Yellow',
                   '120': 'Orange',
                   '121': 'Yellow',
                   '122': 'Yellow',
                   '200': 'Red',
                   '201': 'Red',
                   '202': 'Red',
                   '210': 'Blue',
                   '211': 'Blue',
                   '212': 'Red',
                   '220': 'Purple',
                   '221': 'Purple',
                   '222': 'Purple',
                   },
               'Windflower':{'000': 'White',
                   '001': 'White',
                   '002': 'Blue',
                   '010': 'Orange',
                   '011': 'Orange',
                   '012': 'Blue',
                   '020': 'Orange',
                   '021': 'Orange',
                   '022': 'Orange',
                   '100': 'Red',
                   '101': 'Red',
                   '102': 'Blue',
                   '110': 'Pink',
                   '111': 'Pink',
                   '112': 'Pink',
                   '120': 'Orange',
                   '121': 'Orange',
                   '122': 'Orange',
                   '200': 'Red',
                   '201': 'Red',
                   '202': 'Purple',
                   '210': 'Red',
                   '211': 'Red',
                   '212': 'Purple',
                   '220': 'Pink',
                   '221': 'Pink',
                   '222': 'Purple',
                   },
               'Mum':{'000': 'White',
                   '001': 'White',
                   '002': 'Purple',
                   '010': 'Yellow',
                   '011': 'Yellow',
                   '012': 'White',
                   '020': 'Yellow',
                   '021': 'Yellow',
                   '022': 'Yellow',
                   '100': 'Pink',
                   '101': 'Pink',
                   '102': 'Pink',
                   '110': 'Yellow',
                   '111': 'Red',
                   '112': 'Pink',
                   '120': 'Purple',
                   '121': 'Purple',
                   '122': 'Purple',
                   '200': 'Red',
                   '201': 'Red',
                   '202': 'Red',
                   '210': 'Purple',
                   '211': 'Purple',
                   '212': 'Red',
                   '220': 'Green',
                   '221': 'Green',
                   '222': 'Red',
                   }
               }
    return genetic[flower]


def find_color(gen, flower):
    return gens_with_colors(flower)[gen]


def gen_to_ter(gen):
    t = 2
    n = len(gen)
    ref_letter = ['rr', 'yy', 'ww', 'bb']
    list_gen = [(gen[i:i + t]) for i in range(0, n, t)]

    valid = 1
    for i in range(0, int(n/2)):
        print(ref_letter[i], list_gen[i], n)
        if ref_letter[i] != list_gen[i].lower() or n % 2 == 1:
            valid = 0
            print('Invalido')
    if valid:
        ter = ''.join(('2' if g.isupper() else '0' if g.islower() else '1') for g in list_gen)
    else:
        ter = '3'*n

    return ter


def ter_to_gen(ter):
    letters = ['r', 'y', 'w', 'b']
    gen = ''
    i = 0
    for x in ter:
        opc = {'0': letters[i]+letters[i],
               '1': letters[i].upper()+letters[i],
               '2': letters[i].upper()+letters[i].upper()}
        gen = gen + opc[x]
        i += 1
    return gen


def unique(lista):
    unique_vals = []
    for x in lista:
        if x not in unique_vals:
            unique_vals.append(x)
    return unique_vals

