import argparse
import logging

logger = logging.getLogger(__name__)

def setup_logging(log_file_path, log_level):
    log_level_map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR
    }

    logging.basicConfig(
        filename=log_file_path, 
        level=log_level_map.get(log_level, "INFO"),
        format="%(asctime)s %(levelname)s %(filename)s %(name)s %(lineno)s: %(message)s"
    )

def parse_input_file(input_file_path):
    try:
        with open(input_file_path, 'r') as f:
            file_lines = f.readlines()
            file_lines_clean = [x.strip() for x in file_lines]

            return file_lines_clean
    except Exception as e:
        logger.exception(f"Failed to parse input file")

        raise Exception("Failed to parse input file") from e

def write_output(output_file_path, output_data):
    try:
        with open(output_file_path, 'w') as f:
            for datum in output_data:
                f.write(datum)
                f.write("\n")

    except Exception as e:
        logger.exception(f"Failed to write output file")

        raise Exception("Failed to write to output file") from e


def business_logic():
    return ['Test1', 'Test2']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file-path', help='Input File Path', required=True)
    parser.add_argument('-o', '--output-file-path', help='Output File Path', required=True)
    parser.add_argument('-l', '--log-file-path', help='Log File Path', default="./log.out", required=False)
    parser.add_argument('-ll', '--log-level', help='Log Level', choices=["DEBUG", "INFO", "WARNING", "ERROR"], default="INFO", required=False)

    args = parser.parse_args()

    setup_logging(args.log_file_path, args.log_level)
    
    logger.info(
        "Evaluation script started "
        f"input_file_path={args.input_file_path} "
        f"output_file_path={args.output_file_path} "
        f"log_file_path={args.log_file_path} "
        f"log_level={args.log_level}"
    )

    inputs = parse_input_file(args.input_file_path)

    logger.info(
        "Completed parsing inputs"
    )

    results = business_logic()

    logger.info(
        "Finished processing business logic"
    )

    write_output(args.output_file_path, results)

    logger.info(
        "Finished writing output"
    )

if __name__ == "__main__":
    main()
