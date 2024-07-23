# Coco Dataset Filter for 9 Classes

## Synopsis

This script filters the COCO dataset to include only specific classes, allowing you to train a neural network on a smaller subset of data.

## Installation

1. Clone this repository:

```bash
git clone [https://github.com/](https://github.com/)itzikChaver/coco-classes-filter.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To filter the COCO dataset to the 9 selected classes, run the following command:

```bash
python3 coco_classes_filtering_script.py.py 
```
The script will access the train2017 folder and perform a filter on all the files in it and save them in a new folder named "filter_train2017" and change the name of the original folder to original_train2017

## Classes Included

The script filters the COCO dataset to include the following 9 classes:

* **0: person**
* **1,3: two-wheeler**
* **2: car**
* **7: truck**
* **16: bird**
* **15: cat**
* **16: dog**
* **18: sheep**

## Disclaimer

This script is provided as-is and is not affiliated with the COCO dataset or its creators. Use it at your own risk.

## Contributing

Contributions are welcome! Feel free to fork this repository, make changes, and submit pull requests.

