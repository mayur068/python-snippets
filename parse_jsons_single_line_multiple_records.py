import json
import re

def standardize(text_line):
    """
    This function identified additional data on single line
    and continues to parse recursively until it parses all JSONs
    
    Parameters
    text_line: Single line containing multiple valid JSON records 
    
    Returns
    output_line: Multiple lines having each JSON record on new line
    """
    try:
        json.loads(text_line)
        output_line = text_line
    except json.decoder.JSONDecodeError as e:
        failure = re.search(pattern=r"^Extra data.*$", string=str(e))
        if failure is not None:
            output_line = text_line[0:int(e.pos)] + "\n" + standardize(text_line[int(e.pos):])
    except Excpetion as e:
        print("Error occurred while parsing JSON.")
        print("Versions supported: 3.5 and later")
        print(str(e))
    
    return output_line


def main():
    data_directory = "data/"
    input_file_name = "jsons_single_line_multiple_records.json"
    try:
        with open(data_directory+input_file_name) as inp:
            text_line = inp.readLine()
            output = standardize(text_line)
            print("Output JSON records")
            print(output)
    except FileNotFoundError as e:
        print("Error occurred while reading " + input_file_name)
        print(str(e))
    except Exception as e:
        print("Error Occurred while parsing " + input_file_name)
        print(str(e))


if __name__ == "__main__":
    main()
