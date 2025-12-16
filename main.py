import extract
import transform
import load


def main():
    print("Extracting data...")
    try:
        df = extract.extract()
        print("Transforming data...")
        data = transform.process(df)
        print("Loading data...")
        load.load_to_excel(data)
        print("Done!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
