import os
import tkinter as tk
from tkinter import messagebox

base_classes = [
    'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
    'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
    'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
    'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
    'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
    'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
    'hair drier', 'toothbrush'
]

# Default values
default_filtered_classes = ['person', 'two-wheeler', 'car', 'bus', 'truck', 'bird', 'cat', 'dog', 'sheep']
default_allowed_numbers = {0, 1, 2, 3, 7, 14, 15, 16, 18}
default_replacements = {3: 1, 4: 3, 7: 4, 14: 5, 15: 6, 16: 7, 18: 8}

def get_filtered_classes():
    selected_classes = []
    root = tk.Tk()
    root.title("Select Classes to Keep")

    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    class_vars = []
    for idx, cls in enumerate(base_classes):
        var = tk.IntVar(value=0)
        chk = tk.Checkbutton(frame, text=cls, variable=var)
        chk.grid(row=idx//2, column=idx%2, sticky='w')
        class_vars.append(var)

    def on_submit():
        nonlocal selected_classes
        selected_classes = [cls for cls, var in zip(base_classes, class_vars) if var.get() == 1]
        root.destroy()

    btn_submit = tk.Button(root, text="Submit", command=on_submit)
    btn_submit.pack(pady=10)

    root.mainloop()
    return selected_classes

def get_user_choice():
    """
    Presents a message box to ask the user about default values or manual selection.

    Returns:
        str: "yes" if user chooses default values, "no" otherwise.
    """

    user_choice = messagebox.askquestion(title="Choose Selection", message="Use default values or choose manually?")
    return user_choice.lower()

def on_choose_manually():
    """
    Creates a window with checkboxes for manual selection and updates variables.

    Returns:
        list, set, dict: Updated filtered_classes, allowed_numbers, and replacements.
    """
    root = tk.Tk()
    root.title("Select Classes")

    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    class_vars = []
    for idx, cls in enumerate(base_classes):
        var = tk.IntVar(value=0)
        chk = tk.Checkbutton(frame, text=cls, variable=var)
        chk.grid(row=idx // 2, column=idx % 2, sticky='w')
        class_vars.append(var)

    def on_submit():
        """Retrieves user-selected classes and calculates derived values."""
        selected_classes = [cls for cls, var in zip(base_classes, class_vars) if var.get() == 1]
        new_allowed_numbers = {i for i, cls in enumerate(base_classes) if cls in selected_classes}
        replacements = {i: idx for idx, i in enumerate(new_allowed_numbers)}

        return selected_classes, new_allowed_numbers, replacements

    btn_submit = tk.Button(root, text="Submit", command=on_submit)
    btn_submit.pack(pady=10)

    selected_classes, allowed_numbers, replacements = on_submit()
    root.destroy()
    return selected_classes, allowed_numbers, replacements

# Call functions based on user choice
user_choice = get_user_choice()
print(f"user_choice (after call): {user_choice}")

if user_choice == "yes":
    # Use default values
    print("Use default values")
    # global filtered_classes, allowed_numbers, replacements
    filtered_classes = default_filtered_classes.copy()
    allowed_numbers = default_allowed_numbers.copy()
    replacements = default_replacements.copy()
else:
    # Open window for manual selection
    print("Open window for manual selection")
    filtered_classes = get_filtered_classes()
    allowed_numbers = {i for i, cls in enumerate(base_classes) if cls in filtered_classes}
    replacements = {i: idx for idx, i in enumerate(allowed_numbers)}

# Use the updated variables (if needed)
print("Filtered Classes:", filtered_classes)
print("Allowed Numbers:", allowed_numbers)
print("Replacements:", replacements)

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

    # --- For train folder --- #

    train_input_folder = 'train2017'  # Adjust this path to your input folder
    train_output_folder = 'filter_train2017'

    os.makedirs(train_output_folder, exist_ok=True)  # Create train output folder if it doesn't exist
    train_files_count = 0

    for filename in os.listdir(train_input_folder):
        if filename.endswith('.txt'):
            input_file = os.path.join(train_input_folder, filename)
            output_file = os.path.join(train_output_folder, filename)
            
            process_file(input_file, output_file)

            train_files_count += 1

    print(f"\nThe number of train files scanned is: {train_files_count}\n")
    os.rename(train_input_folder, 'original_train2017')  # Rename train input folder

    # Check for invalid numbers after filtering
    check_invalid_numbers(train_output_folder)

    os.rename(train_output_folder, 'train2017')  # Rename train output folder


    # --- For val folder --- #

    val_input_folder = "val2017"
    val_output_folder = "filter_val2017"

    os.makedirs(val_output_folder, exist_ok=True)  # Create val output folder if it doesn't exist

    val_files_count = 0

    for filename in os.listdir(val_input_folder):
        if filename.endswith('.txt'):
            input_file = os.path.join(val_input_folder, filename)
            output_file = os.path.join(val_output_folder, filename)
            
            process_file(input_file, output_file)

            val_files_count += 1

    print(f"\nThe number of val files scanned is: {val_files_count}\n")

    os.rename(val_input_folder, 'original_val2017')  # Rename val input folder

    # Check for invalid numbers after filtering
    check_invalid_numbers(val_output_folder)

    os.rename(val_output_folder, 'val2017')  # Rename val output folder

    # Update COCO YML file with filtered class information
    coco_yml_path = os.path.join('../..', 'coco.yaml')
    update_coco_yml(coco_yml_path)

    print("script finished successfully")

    example_training_command = "python3 train.py --workers 8 --device 0 --batch-size 4 --data data/coco.yaml --img 3840 3840 --cfg cfg/training/yolov7-tiny.yaml --weights '' --name yolov7-itzik --hyp data/hyp.scratch.tiny.yaml --epochs 1"
    print(f"Example training command: {example_training_command}")

if __name__ == "__main__":
    main()
