# DIG5508 Lab 1

Due October 9

This lab has three parts:

1. Input and Testing Values
2. Writing Functions

The lab reviews concepts introduced in Chapters 1-7 of *Exploratory Programming from the Humanities*. Its goal is to provide practice in reading and writing code.

To turn in the assignment, commit and push the modified .pynb files to your lab1 subdirectory.

# Getting Started

First, make sure you have your local GitHub repository folder open in VS Code.

Then, create a subdirectory for this lab. You can do this either in VS Code through selecting the new folder icon above the folder name, or in a terminal (Ctrl+Shift+\` [tilde] or Cmd+Shift+\`) using the following command:

```bash
$ mkdir lab1
```

Next, download the two Jupyter Notebooks from the class repository: 

[lab1 Jupyter Notebook](https://raw.githubusercontent.com/lucidbard/dig5508-fall19/master/lab1/part1.ipynb)

Save it in the lab1 directory. You can then import the notebook using VS Code by running the command `Python: Import Jupyter Notebook` using `Ctrl+Shift+P` or `Command+Shift+P`.

---

## Part 1: Programming Concepts Review

In [Part 1](./part1.ipynb), we will review each programming concept with examples, including *variables*, *functions*, *iteration* and *conditionals*. You will finish by writing a new function that combines the various concepts.

# Submission
You can export the file (`lab1.py`, if you saved it under that name) using the command pallette: "Python: Export Current Python File As Jupyter Notebook"

To submit, you should either run the following commands from the integrated terminal in VS code, or use the Git tab on the left to add the files, commit and push:

1. Add files to the stage
```bash
git add *
```
2. Make sure that both `lab1/part1.ipynb` are included in the commit:
```bash
git status
```

[](../images/lab1-gitfiles.png)


3. Create a commit with a message
```bash
git commit -m "Lab 1 submission"
```
4. Push the commit to your GitHub repository, using your credentials as necessary:
```bash
git push
```
