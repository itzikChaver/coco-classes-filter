# Coco Dataset Filter 

## Table of Contents
1. [Synopsis](#synopsis)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
   1. [Script Workflow](#script-workflow)
   2. [Script Functions](#script-functions)
5. [Disclaimer](#disclaimer)
6. [Contributing](#contributing)
7. [License](#license)

## Synopsis

This project provides a script to filter and modify the COCO dataset based on user-selected classes. It uses a graphical user interface (GUI) to allow users to select the classes they want to keep, and it updates the COCO dataset configuration file accordingly.

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

1. Place the script in your project directory.
2. Ensure you have the COCO dataset and the `coco.yaml` configuration file in the appropriate directories.
3. Run the script using the following command:

```bash
python3 coco_classes_filtering_script.py
```

The script will access the `train2017` folder, perform a filter on all the files in it, save them in a new folder named `filter_train2017`, and change the name of the original folder to `original_train2017`.

### Script Workflow

1. **GUI for Class Selection:** The script opens a GUI window where users can select the classes they want to keep from the base COCO classes.
2. **Processing Files:** The script processes the COCO dataset files, filters the selected classes, and updates the files.
3. **Update COCO YAML:** The script updates the `coco.yaml` configuration file to reflect the filtered classes.
4. **Error Checking:** The script checks for any invalid numbers in the filtered files to ensure data integrity.

### Script Functions

#### `get_filtered_classes()`
Opens a GUI window to allow users to select classes to keep from the base COCO classes.

#### `process_file(input_file, output_file)`
Processes a single file, filtering and replacing numbers as instructed.

#### `check_invalid_numbers(output_folder)`
Checks filtered files for invalid numbers (outside the range 0-8).

#### `update_coco_yml(coco_yml_path)`
Modifies the COCO dataset configuration file (`coco.yaml`) to reflect the filtered class information.

#### `main()`
Manages the overall workflow of filtering, copying, renaming, and error checking.

## Disclaimer

This script is provided as-is and is not affiliated with the COCO dataset or its creators. Use it at your own risk.

## Contributing

If you want to contribute to this project, please fork the repository and create a pull request with your changes. Make sure to include a detailed description of what you've done and why it's necessary.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

