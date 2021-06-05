# DegreeAverageCalculator

This is a calculator for the Degree Average of a Bachelor Degree.

## Requirements

This app is written in Python using the numpy and pandas modules.
To use it, they need to be installed.

### Linux

```bash
sudo apt install python3 python3-pip
```

Now, the latest version of Python 3 is installed, as well as the latest version of pip, which is a package manager for Python.

```bash
pip3 install numpy pandas
```

Now, the program is ready to be used.

### Windows

To install Python in Linux, download it from [here](https://www.python.org/downloads/). Next, install numpy and pandas by opening the Command Line or Powershell and run

```bash
pip install numpy pandas
```

## How to run

The program has 2 files, DegreeAverageCalculator.py and Classes.csv. The py file is the program itself, while Classes.csv is the file in which the program reads the info. It needs to be configured. LibreOffice Calc can be used, Excel and other alternatives can work, but they are not tested. Add your grade in the third row and if it is an Elective Course and you want the extra info, add in the first row the name of the class and on the second row the class code.
When the file is configured, use this command on the shell.

```bash
python3 DegreeAverageCalculator.py # If it's Debian/Ubuntu
python DegreeAverageCalculator.py # If it's Windows
```

## Disclaimer

Even though this program is created for my studies, if your degree average is also calculated by the ECTS, feel free to use it as well. Otherwise, you can fork the project and change the way the degree is calculated.
On more info on how it is created, please refer to [the documentation](README.adoc).
