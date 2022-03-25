def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('value')
    args = parser.parse_args()
    print(args.value)
