# Добавьте логирование ошибок и полезной информации. 
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import argparse
import csv
import random
import logging

def generate_csv(filename, rows):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Number 1', 'Number 2', 'Number 3'])  # Write the header

            for _ in range(rows):
                row = [random.randint(1, 1000) for _ in range(3)]  # Generate random numbers
                writer.writerow(row)

        print(f'CSV file "{filename}" with {rows} rows has been generated.')
    except Exception as e:
        logging.error(f"Error generating CSV file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", type=str, default='random_numbers.csv', help="CSV filename")
    parser.add_argument("--rows", type=int, default=random.randint(100, 1000), help="Number of rows")
    args = parser.parse_args()

    try:
        generate_csv(args.filename, args.rows)
    except Exception as e:
        logging.error(f"Error: {e}")
