import ast

import pandas as pd


def extract():
    data = list()
    clean_data = list()

    with open("./berries_sales.csv") as fd:
        for line in fd:
            data.append([x.strip() for x in line.split(";")])

    for x in data:
        [clean_data.append(ast.literal_eval(y)) for y in x]

    df = pd.DataFrame(clean_data)
    return df


def main():
    print(extract())


if __name__ == "__main__":
    main()
