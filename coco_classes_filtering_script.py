import os

filtered_classes = ['person', 'two-wheeler', 'car', 'bus', 'truck', 'bird', 'cat', 'dog', 'sheep']
allowed_numbers = {0, 1, 2, 3, 7, 14, 15, 16, 18}
replacements = {3: 1, 4: 3, 7: 4, 14: 5, 15: 6, 16: 7, 18: 8}

def process_file(input_file, output_file):
    """
    Processes a single file, filtering and replacing numbers as instructed.

    Args:
        input_file (str): Path to the input file to be processed.
        output_file (str): Path to the output file where the filtered data will be written.
    """

    filtered_lines = 0
    skipped_lines = 0
    replaced_lines = 0

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            try:
                first_number = int(line.split()[0])

                # Check if the first number needs processing (replacement or removal)
                if first_number in allowed_numbers:
                    if first_number in replacements:
                        # Replace the number
                        line = line.replace(str(first_number), str(replacements[first_number]), 1)
                        replaced_lines += 1
                        print(f"Replaced line in {input_file}: {line.strip()}")
                    outfile.write(line)  # Write line if it's allowed (with or without replacement)
                    filtered_lines += 1
                else:
                    # Skip lines with numbers outside the allowed range
                    skipped_lines += 1
                    print(f"Skipped line in {input_file}: {line.strip()}")
            except (ValueError, IndexError):
                # Handle potential errors during processing (e.g., non-numeric first element)
                skipped_lines += 1
                print(f"Error: Skipping line due to error in {input_file}: {line.strip()}")

    print(f"Processing complete for {input_file}:")
    print(f"- Filtered lines: {filtered_lines}")
    print(f"- Skipped lines: {skipped_lines}")
    print(f"- Replaced lines: {replaced_lines}\n")
def check_invalid_numbers(output_folder):
    """
    Checks filtered files for invalid numbers (outside the range 0-8).

    Args:
        output_folder (str): Path to the folder containing the filtered files.

    Raises:
        ValueError: If an invalid number is found in a file.
    """

    for filename in os.listdir(output_folder):
        if filename.endswith('.txt'):
            output_file = os.path.join(output_folder, filename)
            with open(output_file, 'r') as outfile:
                for line in outfile:
                    first_number = int(line.split()[0])
                    if first_number < 0 or first_number > 8:
                        raise ValueError(f"Invalid number {first_number} found in {output_file}")
            print(f"Successfully checked {filename} for invalid numbers.")  # New print statement

def update_coco_yml(coco_yml_path):
    """
    Modifies the COCO dataset configuration file (`coco.yaml`) to reflect the filtered class information.

    Args:
        coco_yml_path (str): Path to the COCO dataset configuration file (coco.yaml).

    Updates `nc:` and `names:` fields in `coco.yaml` to match filtered classes.
    """

    absolute_coco_yml_path = os.path.abspath(coco_yml_path)
    print(f"coco_yml_path: {coco_yml_path}")
    print(f"absolute_coco_yml_path: {absolute_coco_yml_path}")

    print("Checking existence of file...")
    if not os.path.exists(absolute_coco_yml_path):
        print(f"Error: COCO dataset configuration file ({absolute_coco_yml_path}) not found.\n")
        return

    print("Checking readability of file...")
    if not os.access(absolute_coco_yml_path, os.R_OK):
        print(f"Error: COCO dataset configuration file ({absolute_coco_yml_path}) is not readable.\n")
        return

    print("File exists and is readable.")

    try:
        # Create a backup of the original file
        with open(absolute_coco_yml_path, 'r') as infile:
            content = infile.read()
            with open(absolute_coco_yml_path + '.bak', 'w') as backup_file:
                backup_file.write(content)

        # Read the original file content
        with open(absolute_coco_yml_path, 'r') as infile:
            lines = infile.readlines()

        # Write the modified content to the original file
        with open(absolute_coco_yml_path, 'w') as outfile:
            for line in lines:
                if line.startswith('nc:'):
                    outfile.write(f"nc: {len(filtered_classes)}\n")
                elif line.startswith('names:'):
                    outfile.write(f"names: {filtered_classes}\n")
                    break  # Stop writing after the names line
                else:
                    outfile.write(line)

        print(f"Successfully updated COCO dataset configuration ({absolute_coco_yml_path}) for {len(filtered_classes)} classes.\n")
    except FileNotFoundError:
        print(f"Error: COCO dataset configuration file ({absolute_coco_yml_path}) not found.\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")

def main():
    """
    Manages the overall workflow of filtering, copying, renaming, and error checking.
    """

    input_folder = 'train2017'  # Adjust this path to your input folder
    output_folder = 'filter_train2017'

    os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist

    count = 0

    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename)
            
            process_file(input_file, output_file)

            count = count + 1

    print(f"\nThe number of files scanned is: {count}\n")

    # Update COCO YML file with filtered class information
    coco_yml_path = os.path.join('../..', 'coco.yaml')
    update_coco_yml(coco_yml_path)

    os.rename(input_folder, 'original_train2017')  # Rename input folder

    # Check for invalid numbers after filtering
    check_invalid_numbers(output_folder)

    os.rename(output_folder, 'train2017')  # Rename input folder

    print("script finished successfully")

if __name__ == "__main__":
    main()

# python3 train.py --workers 32 --device 0 --batch-size 32 --data data/coco.yaml --img 3840 3840 --cfg cfg/training/yolov7.yaml --weights '' --name yolov7-itzik --hyp data/hyp.scratch.tiny.yaml --epochs 1
