# Coco Dataset Filter 

## Table of Contents
1. [Synopsis](#synopsis)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
   - [Step 1: Prepare the COCO Dataset](#step-1-prepare-the-coco-dataset)
   - [Step 2: Run the Script](#step-2-run-the-script)
   - [Step 3: Choose Filtering Option](#step-3-choose-filtering-option)
      - [Default Values](#default-values)
      - [Manual Selection](#manual-selection)
   - [Step 4: Process the Files](#step-4-process-the-files)
   - [Step 5: Update COCO Configuration](#step-5-update-coco-configuration)
5. [Script Details](#script-details)
   - [Script Structure](#script-structure)
   - [Script Usage Example](#script-usage-example)
   - [Error Handling](#error-handling)
6. [Disclaimer](#disclaimer)
7. [Contributing](#contributing)
8. [License](#license)

## Synopsis

This project provides a script to filter and modify the COCO dataset based on user-selected classes. It uses a graphical user interface (GUI) to allow users to select the classes they want to keep, and it updates the COCO dataset configuration file accordingly. 
The script provides an option to use default filtering values or to manually select the classes you want to keep.

## Prerequisites

- Python 3.x
- Tkinter (for the GUI)
- `os` module (standard in Python)
- Ensure you have the COCO dataset and the `coco.yaml` configuration file available.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/itzikChaver/coco-classes-filter.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To filter the COCO dataset to the selected classes, follow these steps:

### Step 1: Prepare the COCO Dataset

Ensure that the COCO dataset (train2017 and val2017) is available in the same directory as the script or adjust the paths accordingly.
Ensure you have the COCO dataset and the `coco.yaml` configuration file in the appropriate directories.

### Step 2: Run the Script

Run the script using Python:

```sh
python3 coco_classes_filtering_script.py
```

### Step 3: Choose Filtering Option

The script will prompt you with a message box asking whether to use default values or to choose manually:

- **Default Values**: Select "Yes" to use pre-defined default values for filtering.
- **Manual Selection**: Select "No" to manually choose the classes you want to keep.

#### Default Values

The default filtered classes and their replacements are as follows:

- Filtered Classes: `['person', 'two-wheeler', 'car', 'bus', 'truck', 'bird', 'cat', 'dog', 'sheep']`
- Allowed Numbers: `{0, 1, 2, 3, 7, 14, 15, 16, 18}`
- Replacements: `{3: 1, 4: 3, 7: 4, 14: 5, 15: 6, 16: 7, 18: 8}`

#### Manual Selection

If you choose to manually select classes, a GUI window will appear with checkboxes for each class. Select the classes you want to keep and click "Submit".

### Step 4: Process the Files

The script will process the files in the `train2017` and `val2017` directories, filtering and replacing class labels as specified. The filtered files will be saved in new directories (`filter_train2017` and `filter_val2017`), and the original directories will be renamed.

### Step 5: Update COCO Configuration

The script will also update the `coco.yaml` file with the new class information. Ensure the path to `coco.yaml` is correct in the script.

## Example Training Command

After filtering the dataset, you can train your model using the updated COCO dataset. Here is an example training command:

```bash
python3 train.py --workers 8 --device 0 --batch-size 4 --data data/coco.yaml --img 3840 3840 --cfg cfg/training/yolov7-tiny.yaml --weights '' --name yolov7-itzik --hyp data/hyp.scratch.tiny.yaml --epochs 1
```

## Script Details

### Script Structure

The script consists of the following key functions:

- `get_filtered_classes()`: Opens a GUI window for selecting classes to keep.
- `get_user_choice()`: Asks the user whether to use default values or manual selection.
- `on_choose_manually()`: Handles manual class selection.
- `process_file(input_file, output_file)`: Processes a single file, filtering and replacing class labels.
- `check_invalid_numbers(output_folder)`: Checks for invalid numbers in filtered files.
- `update_coco_yml(coco_yml_path)`: Updates the `coco.yaml` file with new class information.
- `main()`: Manages the overall workflow of filtering, renaming, and error checking.

### Script Usage Example

Here's a simple example of how to use the script:

```sh
python3 coco_classes_filtering_script.py
```

Upon running the script, follow the prompts to choose between default or manual class selection, and let the script process and update the COCO dataset accordingly.

### Error Handling

The script includes error handling for file reading and processing. If an error occurs, the script will skip the problematic line and continue processing the rest of the file.

## Disclaimer

This script is provided as-is and is not affiliated with the COCO dataset or its creators. Use it at your own risk.

## Contributing

If you want to contribute to this project, please fork the repository and create a pull request with your changes. Make sure to include a detailed description of what you've done and why it's necessary.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

