import argparse
import random


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--probability",
        type=float,
        help="the probability of a reward",
        default=0.5,
    )

    args = parser.parse_args()
    p = args.probability

    if random.random() < p:
        print("Go reward yourself!")
    else:
        print("No reward this time.")


if __name__ == "__main__":
    main()
