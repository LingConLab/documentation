## 1. Inroduction

## 2. General 

### 2.1 Description
It is nice to start your code or create a README.md file with a short description containing:

* name of the author/authors
* date of the creation
* project link with the ConLab affiliation
* general purpose of the script
* link to the github, where the latest version is stored
* licence

```
# This is code to replicate the analyses and figures from article [Abced, Hij 2019]
# 2019.03.08 J. Rscripter, M. Pythonscripter (HSE Linguistic Convergence Laboratory)
# This script is distributed under the GNU General Public License.
# The last vertion of this script is here: https://...
```

### 2.2 File names
File names should be meaningful. Avoid using special characters (Cyrillic, IPA) in file names --- stick with numbers, standard Latin letters, -, and _. Avoid using transliterated names (like `danniye_iz_Rikvani.txt`) or, if you ought to (like for word-specific files, e. g. sound name for one word), add English translation (bad: `2019.03.14_Neshukay_Adyghe_shha.wav`, good: `2019.03.14_Neshukay_Adyghe_head_shha.wav`). If files should be run in a particular order, prefix them with numbers. If it seems likely you’ll have more than 10 files, left pad with zero (`01.bla-bla...`, `02.bla-bla...`, ... `09.bla-bla...`, `10.bla-bla...`...). Pay attention to capitalization, since you, or some of your collaborators, might be using an operating system with a case-insensitive file system, so **never** use names that differ only in their capitalization.

## 3. Github Repos

## 4. DBs

## 5. Sites and Platforms

## 6. Python

If you create scripts, applications or libraries using Python, you should provide comments in your code.
The best way do is to use docstrings which can be easily accessed with `<name>.__doc__`
You should describe every module, function, class and method (what is it for, how it works, why it is there).
For modules you also shoud provide list of variables and their description.
For classes you should provide list of variables, attributes and their description.
For functions and methods you should provide list of parameters and the output.

We provide the example in `documented_python.py` in this repo.

## 7. R
### 7.1 Libraries
List all libraries at the begining (don't use `require()` function):

```
library(tidyverse)
library(lingtypology)
```

Superheroes could also use `packageVersion()` function and report verssions of the packages.

```
library(tidyverse) # v. 1.2.1
library(lingtypology) # v. 1.0.13
```

### 7.2 `setwd()`
Be careful when using `setwd()`. Usage of the absolute path (like `"/Users/Alladin/Documents/sannic-project/files/"`) can limit reproducibility. It is the same about reading and writing files in a script (like `read.csv(file = "/Users/Alladin/Documents/sannic-project/files/dataset-2013-01.csv")`).

### 7.3 Temporary objects
For long codes it is a good practice to remove temporary objects after they have served their purpose. It will make it easear to debug the code.

## Authors

K. Filatov, G. Moroz, L. Morozova, N. Panova, L. Sokur, M. Voronov
