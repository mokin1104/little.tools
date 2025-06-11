import argparse
from datetime import datetime, timedelta

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(
        description="Subtract seconds from a timestamp and output the new timestamp in YYMMDD-HHMMSS format."
    )

    # Argument for the number of seconds to subtract
    parser.add_argument(
        "--seconds", "-s",
        type=float,
        required=True,
        help="Number of seconds to subtract (e.g., 249890.63)"
    )

    # Argument for the original timestamp in the format YYMMDD-HHMMSS
    parser.add_argument(
        "--timestamp", "-t",
        type=str,
        required=True,
        help="Original timestamp in YYMMDD-HHMMSS format (e.g., 250610-163134)"
    )

    # Parse the arguments
    args = parser.parse_args()

    try:
        # Convert timestamp string to datetime object
        original_time = datetime.strptime(args.timestamp, "%y%m%d-%H%M%S")

        # Subtract the specified number of seconds
        new_time = original_time - timedelta(seconds=args.seconds)

        # Output the new timestamp in the same format
        print(new_time.strftime("%y%m%d-%H%M%S"))

    except Exception as e:
        # Print any error that occurs during processing
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
