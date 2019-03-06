## General 

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

## Github Repos

## DBs

## Sites and Platforms

## Python

If you create scripts, applications or libraries using Python, you should provide comments in your code.
The best way do is to use docstrings which can be easily accessed with `<name>.__doc__`
You should describe every module, function, class and method (what is it for, how it works, why it is there).
For modules you also shoud provide list of variables and their description.
For classes you should provide list of variables, attributes and their description.
For functions and methods you should provide list of parameters and the output.

We provide the example in `documented_python.py` in this repo.

## R
### Libraries
List all libraries at the begining (don't use `require()` function):

```
library(tidyverse)
library(lingtypology)
```

### `setwd()`
Be careful when using `setwd()`. Usage of the absolute path (like `"/Users/Alladin/Documents/sannic-project/files/"`) can limit reproducibility. It is the same about reading and writing files in a script (like `read.csv(file = "/Users/Alladin/Documents/sannic-project/files/dataset-2013-01.csv")`).


## Authors

K. Filatov, G. Moroz, L. Morozova, N. Panova, L. Sokur, M. Voronov
