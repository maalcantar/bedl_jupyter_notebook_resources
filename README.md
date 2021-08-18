# BEDL Jupyter Notebook Resources

## Why should I use a Jupyter notebook?
There are many ways to write reproducible code. While editors like PyCharm and RStudio offer similar, notebook-based coding environments, Jupyter Notebook is one of the most popular ways to interact with, share, and write code. If you work in a data science field, especially applying computational analyses to biology, chances are you will run into a Jupyter Notebook or Google Colab notebook at least once. Being familiar with the interface is an important skill for many applications, like working on homework for class, depositing your code for a journal article, and more!

Working in a Jupyter Notebook allows you to simultaneously view your code and corresponding outputs, as well as include explanatory text using [Markdown](https://medium.com/analytics-vidhya/the-ultimate-markdown-guide-for-jupyter-notebook-d5e5abf728fd), all in a single document! These features make Jupyter Notebook a useful tool for exploratory data analysis, debugging, and sharing code / results with collaborators. Additionally, there are some nifty features that can help with organizing your coding projects. 

## This repository
This GitHub repository is meant to quickly get you set up and familiarized with Jupyter Notebook, such that you get the most out of Jupyter Notebook while starting up your coding projects! The repository contains the following documents:

<code>README.md</code>: This README document contains useful information for i) [installing Jupyter Notebook via Anaconda](#installing-jupyter-notebook) ii) [installing new packages](#installing-new-packages) iii) [creating and using virtual envionments](#staying-organized-with-virtual-environments) and iv) [using utils.py files](#working-with-a-utilspy-file). The end of the document also contains links to [other useful resources for Jupyter Notebook](#other-great-resources-and-examples).

<code>Frequently_Asked_Questions_About_Jupyter.ipynb</code>: The example notebook contains responses, in the form of code implementations, to several frequently asked questions people have about Jupyter Notebooks. 

If you have any questions or have suggestions for how to improve this repository, please reach out to Jacqueline Valeri (valerij [at] mit.edu), Miguel Alcantar (alcantar [at] mit.edu), or any other BEDL fellow / staff (https://bedatalab.github.io/)!

## Installing Jupyter Notebook 
The easiest way to get started with Jupyter Notebooks is by installing [Anaconda](https://www.anaconda.com/products/individual#Downloads). Anaconda is a popular Python distribution which comes pre-equipped with Jupyter Notebook and makes managing and installing new packages very simple (see [Installing and using new packages section](#installing-new-packages) below). In order to install Anaconda, you should:

1. [Download](https://www.anaconda.com/products/individual#Downloads) the latest version of Anaconda (i.e., Python 3.8 as of May 2021). The installer you download will depend on the specifications of the machine you are using.
2. If you are downloading packages locally, open the .exe file you just downloaded, and follow the instructions.
3. To make sure the installation went smoothly, open your command line and enter.

```bash
jupyter notebook
```
If this opens a new tab in your default web browser with the Jupyter logo in the top-left (see image below) the installation was successful and you should be good to go! If the installation was not successful, double-check to make sure you downloaded the correct installer. 

<img width="1315" alt="Screen Shot 2021-05-16 at 12 12 30 AM" src="https://user-images.githubusercontent.com/43210496/118385243-69a7c500-b5db-11eb-93f2-52959f4b4dd2.png">

Note: If you want to work with an older version of Python, we still recommend you download the latest version of Anaconda and just create a virtual environment with the specific Python version you want. You can technically install an older version of Anaconda / Python from [archives](https://repo.anaconda.com/archive/), but we recommend sticking with the newer version of Anaconda in order to avoid any compatibility issues.

## Installing new packages

One of the many useful features of Anaconda and Jupyter Notebook is that they make installing new packages relatively simple. Packages are openly available modules of code that you can use to perform specific functions in your code. 

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

Once packages are installed, they can be imported and used in Jupyter Notebook. For example, we could use the MatPlotLib library to plot some data --- if you have used Python in the past, you may be familiar with the following block of code:

```python 
import matplotlib.pyplot as plt
plt.plot(x_data, y_data)
plt.show()
```

## Staying organized with virtual environments
Virtual environments are isolated coding environments that can help keep your coding projects organized. In brief, virtual environments are great for managing different projects and the corresponding packages required to run code for each project. Virtual environments can also keep your code reproducible, and can even help avoid package conflicts. We recommend following guidelines from the BEDL virtual environment resource (link to BEDL venv resource here). 

Thankfully, virtual environments interface well with Jupyter Notebook and you can quickly set up a new virtual environment by following these steps in the command line :
1. Create new virtual environment 
```bash
conda create -n bedl_virtual_env python=3.8
```
Note: you can name your virtual environment whatever you want (change the variable after '-n') and also install whatever Python version you want to work with (change the version after 'python='. In the example above, we created a virtual environment called 'bedl_virtual_env' and installed Python version 3.8. After entering this command, the terminal will prompt you and ask whether you want to install some default packages, which you can accept by entering 'y' (which stands for 'yes!')

2. Activate new virtual environment
You can activate the virtual environment using:
```bash
conda activate bedl_virtual_env
```
Similarly, you can deactivate the virtual environment using:

```bash
conda deactivate

```

Note: the virtual environment we created and activated is 'bedl_virtual_env' but your commands will depend on what you named the virtual environment in step 1. For a list of virtual environments you have created, you can use 

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
If you followed these steps, the next time you open Jupyter Notebook you should be able to open notebooks in your new virtual environment: just click "New" in the top-right, and select the virtual environment your want (see image below).

<img width="540" alt="Screen Shot 2021-05-16 at 12 35 44 PM" src="https://user-images.githubusercontent.com/43210496/118404969-3ef15700-b643-11eb-8d74-4dd6621f9ce9.png">

## Working with a utils.py file
Throughout your coding endeavors, you may find yourself performing the same tasks / functions in multiple notebook files. Instead of defining the same function over and over in each notebook file, jupyter notebooks actually let you define the function once in a script (commonly called a utils.py file) and import those functions into each Jupyter notebook. Please see FAQs notebook for an example.

## Other great resources and examples

Hopefully this resource has helped you get set up and familiarized with Jupyter Notebook. This is of course, however, not an exhaustive guide to everything Jupyter Notebook has to offer, so we encourage you to learn more about additional Jupyter Notebook features by checking out some useful online resources:

More introductions to Jupyter Notebook:

- https://realpython.com/jupyter-notebook-introduction/
- https://programminghistorian.org/en/lessons/jupyter-notebooks
- https://www.dataquest.io/blog/jupyter-notebook-tutorial/
- https://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/Notebook%20Basics.ipynb

Example notebook on Google Colab (a platform for collaboratively working with Jupyter Notebooks):

- https://colab.research.google.com/github/jckantor/CBE30338/blob/master/docs/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.ipynb

Additional Jupyter Notebook examples & tutorials: 

- https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks

Advanced Jupyter Notebook tricks:

- https://towardsdatascience.com/bringing-the-best-out-of-jupyter-notebooks-for-data-science-f0871519ca29
