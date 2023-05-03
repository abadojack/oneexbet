import pandas as pd

import argparse


def process_csv(stake_):
    print(f"If you put a stake of Kes {stake_} on all the bet slips posted by Gabriel_gunner2 on twitter in April, 2023:")

    data = pd.read_csv('Gabriel_gunner2.csv')
    total_win = 0.0
    total_loss = 0.0
    win_count, loss_count = 0, 0

    # 7.5% tax on stake
    stake_ *= 0.925
    for index, row in data.iterrows():
        if row['Actual'] == 'Win':
            win_count += 1
            total_win += float(row['Expected']) * stake_
        elif row['Actual'] == 'Loss':
            loss_count += 1
            total_loss += stake_

    print("Number of bet slips won: ", win_count)
    print("Number of bet slips lost: ", loss_count)

    print("Return: ", total_win)
    print("Loss: ", total_loss)

    # 20% tax on winnings
    print("Profit: ", (total_win - total_loss) * .80)
    print("win/loss * 100: ", win_count/loss_count * 100)


def parse_args():
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-s", "--stake", help="Stake")

    # Read arguments from command line
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.stake:
        stake = float(args.stake)

        process_csv(stake)
