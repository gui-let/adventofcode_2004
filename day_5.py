'''Module for solving day 5'''


def read_rules():
    '''read rules file'''
    with open('data/5_rules_sample.txt', 'r', encoding='utf8') as f:
        r = {}
        for row in f:
            k, v = [int(i) for i in row.rstrip().split('|')]
            try:
                r[k].append(v)
            except KeyError:
                r[k] = [v]
    return r


def read_updates():
    '''read updates file'''
    with open('data/5_updates_sample.txt', 'r', encoding='utf8') as f:
        u = []
        for row in f:
            u.append([int(i) for i in row.rstrip().split(',')])
    return u


def verify_updates(rules: dict[list], updates: list[list]) -> tuple[list]:
    '''returns: (right_updates, wrong_updates)'''
    right_updates = []
    wrong_updates = []
    for u in updates:
        for i, p in enumerate(u):
            try:
                r = rules[p]
            except KeyError:
                r = []
            if set(r) & set(u[:i]):
                wrong_updates.append(u)
                break
            if i == len(u) - 1:
                right_updates.append(u)
    return right_updates, wrong_updates


def sum_central_values(updates_to_sum):
    '''sum central values'''
    total = 0
    for u in updates_to_sum:
        total += u[len(u) // 2]
    return total


def solve_part_1(rules: dict[list], updates: list[list]) -> int:
    '''solve part 1'''
    right_updates, _ = verify_updates(rules, updates)
    result = sum_central_values(right_updates)
    return result


if __name__ == '__main__':
    RULES = read_rules()
    UPDATES = read_updates()

    print('part 1:', solve_part_1(RULES, UPDATES))
