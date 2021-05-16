# BEDL Jupyter Notebook Resources

Jupyter notebooks provide a great environment for interactively working with code. Coding in a Jupyter notebooks allows you to simultaneously view your code and corresponding outputs, as well as include explanatory text in the form of markdown, all in a single document! These features make jupyter notebooks a useful tool for exploratory data analysis, debugging code, and sharing code / results with collaborators. 

This GitHub repository is meant to quickly get you set up and familiarized with Jupyter notebook. The structure of this repository is as follows:

<code>README.md</code>: The README document contains useful information for i) [installing Jupyter Notebook via Anaconda](#installing-jupyter-notebook) ii) [installing new packages](installing-new-packages) iii) [creating and using virtual envionments](staying-organized-with-virtual-environments) and iv) [using utils.py files](working-with-a-utils.py-file). The end of the document also contains links to other useful resources for Jupyter Notebook

<code>Frequently_Asked_Questions_About_Jupyter.ipynb</code>: this example notebook contains answers (in the form of code implementations) to several frequently asked questions people have about jupyter notebooks. 

If you have any questions or have suggestions for how to improve this repository, please reach out to Jacqueline Valeri (valerij [at] mit.edu), Miguel Alcantar (alcantar [at] mit.edu), or any other BEDL fellow / staff (https://bedatalab.github.io/). 

## Installing Jupyter Notebook 
The easiest way to get started with Jupyter Notebooks is by installing [Anaconda](https://www.anaconda.com/products/individual#Downloads). Anaconda is a popular Python distribution which comes pre-equipped Jupyter Notebook and makes managing and installing new packages very simple (see [Installing and using new packages section](#installing-and-using-new-packages) below). In order to install Anaconda, you should:

1. [Download](https://www.anaconda.com/products/individual#Downloads) the latest version of Anaconda (i.e., Python 3.8). The installer you download will depend on the specifications of the machine you are using.
2. Open the .exe file you just downloaded, and follow the instructions.
3. To make sure the download went smoothly, open your command line and enter.

```bash
jupyter notebook
```
If this opens a new tab in your default web browser with the Jupyter logo in the top-left, the installation was successful and you should be good to go! If the installation was not successful, double-check to make sure you downloaded the correct installer. 

Quick note: If you want to work with an older version of Python, we still recommend you download the latest version of Anaconda and create a virtual environment with the specific python version you want. You can technically install an older version of Anaconda / python from [archives](https://repo.anaconda.com/archive/), but we recommend sticking with the newer version such that your Anaconda installation is up-to-date. 

## Installing new packages

One of the many nifty features of Anaconda and Jupyter Notebooks is that they make installing new packages relatively simple. Packages are openly available modules of code that you can use to perform specific functions in your code. 

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
1. Create new virtual environment
```bash
conda create -n bedl_virtual_env python=3.8
```
Note: you can name your virtual envionment whatever you want (change the variable after '-n') and also install whatever python version you want to work with (change the verison after 'python='. After entering this command, the terminal will prompt you and ask whether you want to install some default packages, which you can accept by entering 'y' (which stands for 'yes!')

2. Activate new virtual environment
You can activate the virtual environment using:
```bash
conda activate bedl_virtual_env
```
Similarly, you can deactivate the virtual environment using:

```bash
conda deactivate

```

Note: the virtual environment we created and accessed is 'bedl_virtual_env' but your input commands will depend on what you named the virtual environment in step 1. For a list of virtual environments you can created, you can use

```bash
conda env list
````

3. Install ipykernel when your virtual environment is activated
```bash
pip install --user ipykernel
```
4. Add virtual environment to jupyter 
```bash
python -m ipykernel install --user --name=bedl_virtual_env
```
If you followed these steps, the next time you open Jupyter Notebook, you should be able to open a kernel with your new virtual environment

<img width="403" alt="Screen Shot 2021-05-15 at 10 51 10 PM" src="https://user-images.githubusercontent.com/43210496/118383894-10866400-b5d0-11eb-91bf-73bddd3d4854.png">

## Working with a utils.py file
Throughout your coding endeavors, you may find yourself performing the same tasks / functions in multiple notebook files. Instead of created the same function over and over in each notebook file, jupyter notebooks actually let you define the function once in a script (commonly called a utils.py file) and import those functions into each Jupyter notebook. Please see FAQs notebook for an example.

## Other great resources and examples

This resource is not comprehensive, please seee these:

ntros: 
https://realpython.com/jupyter-notebook-introduction/
https://programminghistorian.org/en/lessons/jupyter-notebooks
https://www.dataquest.io/blog/jupyter-notebook-tutorial/

Example notebook on google colab: https://colab.research.google.com/github/jckantor/CBE30338/blob/master/docs/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.ipynb

Solid repo with lots of jupyter notebook examples & tutorials: https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks

Advanced jupyter notebook tricks: https://towardsdatascience.com/bringing-the-best-out-of-jupyter-notebooks-for-data-science-f0871519ca29
