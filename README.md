# BEDL Jupyter Notebook Resources

Jupyter notebooks are a great environment for interactively working with code.

## Installing Jupyter Notebook 
The easiest way to get started with Jupyter Notebooks is by installing [Anaconda](https://www.anaconda.com/products/individual#Downloads). Anaconda is a popular Python distribution which comes pre-equipped with several useful packages (e.g.,  NumPy, pandas, and Matplotlib), and makes installing new packages very simple (see [Installing and using new packages](#installing-and-using-new-packages)). In order to install Anaconda, you should:

1. [Download](https://www.anaconda.com/products/individual#Downloads) the latest version of Anaconda (i.e., Python 3.8). The installer you download will depend on the specifications of the machine you are using.
2. Open the .exe file you just downloaded, and follow the instructions.
3. To make sure the download went smoothly, open your command line and enter.

```bash
jupyter notebook
```
If this opens a new tab in your default web browser with the Jupyter logo in the top-left, the installation was successful and you should be good to go!

Quick note: If you want to work with an older version of Python, we recommend you still download the latest version of Anaconda and create a virtual environment with the specific python version you want. You can technically install an older version of Anaconda / python from [archives](https://repo.anaconda.com/archive/), but we recommend sticking with the newer version such that your Anaconda installation is up-to-date. 

## Installing and using new packages

One of the nifty features of Anaconda and Jupyter Notebooks is that they make installing new packages relatively simple. Packages are essentially openly available modules of code that you can use to perform specific functions in your code. For example, if you have used python in the past, you may be familiar with the following block of code:
```python 
import matplotlib.pyplot as plt
plt.plot(x_data, y_data)
plt.show()
```
In this case, we are importing the matplotlib package (specifically, the collection of methods in pyplot) and then using this package to create a plot of our data. 

Matplotlib is actually one of the packages that is pre-installed by Anaconda. New packages can be installed using the pip command. For instance, the machine learning library PyTorch can be installed by running the following in the command line:


```bash
pip install torch
```
