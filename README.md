# Image_information_embedder

## Overview
This project allows you to embed any file without distorting the image.

### Details
Records and reads 0 and 1 according to the even and odd RGB numbers of the image
Can write and read binary and file names simultaneously in the image itself, so extensions can be applied automatically

## Usage (general users)

### Installation

Download the latest release.

## Usage
Run "Image_information_embedder.exe" included in the release　in zip file.

### Settings

When executed, the following input screen will be displayed

```sh
Mode: Encode or decode: Enter 0 or 1:
```

Select whether to write (0) or read (1) the file
### If you select write

The following input screens will be displayed in sequence. An input example is also shown

(1)
```sh
Enter the file path to save:
```

Description: Select the path of the file to embed.

Example:
```sh
Enter the file path to save: Text.txt
```
(2)
```sh
Enter the file path to output:
```

Description: Enter the file name to output.
It is recommended to avoid the same name and enter the same extension.
A file with this name will be generated when decoded.

Example:
```sh
Enter the file path to save: Text1.txt
```
(3)
```sh
Enter the path of the image to write:
```

Description: Enter the image file name to write.
jpg or png files are recommended.

Example:
```sh
Enter the path of the image to write: Image.png
```
(4)
```sh
Enter the file path to save:
```

Description: Enter the image file name to write.

It is recommended to avoid the same name and enter the same extension.
It must be a png file.

An image file with this name will be generated.

Example:
```sh
Enter the path to the file to save:Image1.png:
```
When all items are entered, in the above case, text.txt will be embedded and the Iimage1.png file will be generated.

## If you select Load
The following input screen will be displayed in sequence. An input example is also shown.

Prerequisites: In this example, Image1.png generated in the writing example above will be loaded.

```sh
Enter the path to the image to load:
```
Explanation:
Select the file to load. The extension must be .png.

Example:

```sh
Enter the path to the image to load:Image1.png
```
When this item is entered, in this example, "text1.txt" will be generated.

## How to use (Developer)
Download with the green button in the upper right.
### Prerequisites
Python must be installed
###Install dependencies
This project depends on the Python module (Pillow).

To install, run

```sh
pip install Pillow
```

.
### How to run

Execute Image_information_embedder.py.

The general method is to go to the downloaded directory and run

```sh
python Image_information_embedder.py
```

### Build

You can do it your own way.

For release, we build with

pyinstaller


## Translation

This explanation and the commented out files are machine translated from Japanese.

There may be don't desirable or incorrect expressions.

In that case, please report it by lssues.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
