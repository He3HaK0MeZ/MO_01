import simplextable as sim_table


if __name__ == '__main__':
    filename = 'data.txt'
    data = [line.replace('\n', '') for line in open(filename)]

    table = sim_table.SimplexTable(data)

    if table.solve():
        table.print_answer(data)
