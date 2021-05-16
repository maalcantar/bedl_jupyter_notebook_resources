# BEDL Jupyter Notebook Resources

Jupyter notebooks are a great environment for interactively working with code.

## Installing Jupyter Notebook 
The easiest way to get started with Jupyter Notebooks is by installing [Anaconda](https://www.anaconda.com/products/individual#Downloads). Anaconda is a popular Python distribution which comes pre-equipped Jupyter Notebook, and makes managing and installing new packages very simple (see [Installing and using new packages section below](#installing-and-using-new-packages)). In order to install Anaconda, you should:

1. [Download](https://www.anaconda.com/products/individual#Downloads) the latest version of Anaconda (i.e., Python 3.8). The installer you download will depend on the specifications of the machine you are using.
2. Open the .exe file you just downloaded, and follow the instructions.
3. To make sure the download went smoothly, open your command line and enter.

```bash
jupyter notebook
```
If this opens a new tab in your default web browser with the Jupyter logo in the top-left, the installation was successful and you should be good to go!

Quick note: If you want to work with an older version of Python, we recommend you still download the latest version of Anaconda and create a virtual environment with the specific python version you want. You can technically install an older version of Anaconda / python from [archives](https://repo.anaconda.com/archive/), but we recommend sticking with the newer version such that your Anaconda installation is up-to-date. 

## Installing new packages

One of the nifty features of Anaconda and Jupyter Notebooks is that they make installing new packages relatively simple. Packages are openly available modules of code that you can use to perform specific functions in your code. 

Packages can be installed using the pip command. For instance, the popular plotting package MatPlotLib can be installed by running the following in the command line:

```bash
pip install matplotlib
```

You can also specify the version number of the package you want to install

```bash
pip install matplotlib==3.4.2
```

Multiple packages can be installed simultaneously by separating each package name by a space

```bash
pip install matplotlib==3.4.2 networkx==2.5.1 scikit-learn==0.24.2
```

Once packages are installed, they can be imported and used in Jupyter Notebook. For example, we could use the MatPlotLib library to plot some data. For example, if you have used python in the past, you may be familiar with the following block of code:

```python 
import matplotlib.pyplot as plt
plt.plot(x_data, y_data)
plt.show()
```
## Staying organized with virtual environments
Virtual environments are isolated environments that can help keep your coding projects organized. In brief, virtual environments are great for managing different projects and the corresponding packages required to run code for each project. In the long-run, virtual environments can also keep your code reproducible, and can even help avoiding package conflicts. See Jackie + Divya's resource for more info (insert hyperlink). 

Thankfully, virtual environments interface well with Jupyter Notebook and you can quickly set up a new virtual environment with a few simple command in the command link:
1. create new virtual environment
```bash
conda create --name bedl_virtual_env python=3.8
```
Note that you can name your virtual envionment whatever you want (change the variable after '--name') and also install whatever python version you want to work with (change the verison after 'python='
