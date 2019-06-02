## About

* K. Filatov, G. Moroz, L. Morozova, N. Panova, L. Sokur, M. Voronov
* Linguistic Convergence Laboratory
* 21 March 2019
* last version could be found [here](https://github.com/LingConLab/documentation/blob/master/README.md).

---

## 1. Inroduction
This is a collection of instruction for digital products created in Linguistic Convergence Laboratory. Of course all products are individual and we didn't have a plan to cover them all. Following these instruction you will help for purposes of:

* reproducibility,
* code debugging,
* code review,
* software reuse.

Our instructions will cover the simplist common mistakes, but for more complicated cases have a look [here](https://en.wikipedia.org/wiki/Anti-pattern#Software_engineering) for a list of anti-patterns for software engineering.

---

## 2. General 

### 2.1 Description
It is nice to start your code or create a `README.md` file with a short description containing:

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
File names should be meaningful. Avoid using special characters (Cyrillic, IPA) in file names --- stick with numbers, standard Latin letters, -, and _. Avoid using transliterated names (like `danniye_iz_Rikvani.txt`) or, if you ought to (like for word-specific files, e. g. sound name for one word), add English translation 

* bad: `2019.03.14_Adyghe_Neshukay_sp4_shha.wav`, 
* good: `2019.03.14_Adyghe_Neshukay_4m1978_head_shha.wav`. 

In example above `4m1978` `4` is an id for the speaker, `m` is a gender of the speaker, `1978` is a year of birth. File naming conventions are depends on team arrangements, so should be discussed within the team. 

If files should be run in a particular order, prefix them with numbers. If it seems likely you’ll have more than 10 files, left pad with zero (`01.bla-bla...`, `02.bla-bla...`, ... `09.bla-bla...`, `10.bla-bla...`...). Pay attention to capitalization, since you, or some of your collaborators, might be using an operating system with a case-insensitive file system, so **never** use names that differ only in their capitalization. If you have multiple files it is better to add to `README.md` specification for each meaningful file containing information about purpose of files, programming language they written (including version) etc.

### 2.3 Code
It is nice to limit your code to 80 characters per line. Long code lines are bad for readability. Also, many people prefer editor windows that are about 80 characters wide.

### 2.4 Comment your code
Just do it.

### 2.5 Tests
If you create a function or even package that will be used multiple times, it is nice to create tests for each function. It is even beter to write some tests before you start creating your function or package.

### 2.6 Warnings
If you create a function or even package it is better to incorporate some argument's check (e. g. Whether some argument is a number? What should the function do with missing values?) and create some meaningfull warning/error messages.

### 2.7 Examples
If you create a function or even package it is nice to write some text that describes every argument in all functions and all classes. It is also important to add some working examples that illustrate what youe functions do.

### 2.8 Citing
Don't forget to cite your data sources and software developers (Python, R, all package creaters). It is also nice to provide information about how to cite your work. If the result of our work is some `.html` page that represents data it is possible to use [GitHub](https://github.com) and [Zenodo](https://zenodo.org/) for obtaining some DOI codes for any stuff that you put in the GitHub repository. For experiments and databases it is also possible to use [OSF](osf.io).

### 2.9 Versioning
Each important change to a function/package should be announced in `NEWS.md`. It is also to nice to have tracking of versions (have a look to [Semantic Versioning](https://semver.org/)).

---

## 3. Github Repos

* It would be better to use laconic names for your GitHub repositories, try to avoid using the full NPs, this information could find its place in the description of a project.

good: `rut_corpus`

bad: `corpus-of-the-rutul-language`

* Use semantically interpretable names

good: `rutul_elicit_db`

bad: `my_article_2018`

* Use only hyphens as the delimiters for the name of your GitHub repository; it is better to avoid using the capitals.

* Provide your repo with a short description in `README.md` file that clarifies the full name and the aim (if needed) of a project. It would be nice if there was a relevant link, for example a link to a web-service which code is stored in your repo.

* Try not to use Laboratory's GitHub for your personal or temporary projects and vice versa

* It is better to use messages provided with git commits reasonably describing what has changed comparing to the previous commit

---

## 4. Databases

You should provide your database with a documentation regardless of the format. Please name tables and columns of your databases relatively to its content.

- `.cvs`, `.xls` tables should have a small description of the whole content. Comment each column on data it contains, e.g.:

> **Cow Dataset**
>
> The current dataset contains information on cows of southern Dagestan area
>
> *id* - unique identificatior of each cow
>
> *age* - the age of a cow at the moment of documentation
>
> *colour* - the colour of fur of a cow

- any kind of relational **SQL** databases should be provided with a description of the way its tables are connected with each other. Also, it would be nice if you mention the format of each column (int, chr, data etc.); each table and colums should have the same kind of comments as you can see above.

It is strongly recommended you to use unique ids as a relational key for tables of your database to simplify its relational structure. 

- **documentary databases** (JSON, XML and management systems like MongoDB or ElasticSearch) should also have comment on what kind of documents it may contain and what structure they have

- any other type of DB should have similiar documentation based on further principle: every key and every value should be decribed.

[Some miraculous example is comming soon...]()

---

## 5. Web applications

If you develop a web application, you should provide:

**system administration manual**

- system requirements (modules, packages, etc.: for example, apache web-server, python 3.6, ssh, mysql)

- access requirements if necessary (password, public key, passphrase, port number)

- links to additional materials (e.g. mysql backup script)

- installation instructions

**functional specification**

- complete code files structure description

- comment your code as much as possible or at least provide an assignment to each file (what does it contains and what purposes does it serve) in your web application. Follow the norm required by programming language you use (e.g. PEP8 for Python)

- if your site contains a database, make additional sub-documentation to it (see section 4)


### 5.1 Platforms

If you consider to use your web application as a platform for other projects, you should provide a manual including:

- contacts of the platform developer

- the way you want users cite your platform in projects

- a link to a repo containing template version of your application

- an instruction for data preparation and composition

- instruction or description of web interface contents to allow a user make changes in site desing in view of purposes of a project (e.g. edit titles and contents of general sections)

- it is nice, if the code of your platform will be commented (the way it described in section 5) to allow users upgrade your platform

You may follow an example given in [`Instruction to dialect corpora platform`](https://github.com/LingConLab/documentation/blob/master/dialect_corpora_platform.md)

---

## 6. Python

### 6.1 Format reqiurements
If you create scripts, applications or libraries using Python, you should follow PEP8 norm rules.

### 6.2 Modules
In README to your python project you should list system requiremets you use: e.g. python version and list of modules.

```
OpenAI Gym 0.10.5
Tensorflow > 13.0.0
MuJoCo 1.50
```

### 6.3 Comments
Comment your code reasonably and as extensively as possible. It would be nice if you give a short description on each module and class you have created. Comment your classes and functions on input/output values if it is necessary. The best way to do this is to use docstrings which can be easily accessed with `<name>.__doc__`, e.g. comment for a function:

```
def build_mlp(input_placeholder, output_size, scope):
    """
        Builds a feedforward neural network
        
        arguments:
            input_placeholder: placeholder variable for the state (batch_size, input_size)
            output_size: size of the output layer
            scope: variable scope of the network
        returns:
            output placeholder of the network (the result of a forward pass)   
    """
    with tf.variable_scope(scope):
        # some code here
    return output_placeholder
```

### 6.4 Compatibility issue
Please name your variables in understandible way in English to make it readable for international co-workers. Make your code as much compatible to other systems as possible, e.g. use `os.path.join` for path variables to make them valid for any OS.

We provide the example in `documented_python.py` in this repo.

---

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

Avoid importing packages as a whole, as this can cause name clashes between the imported packages. Instead, import only the specific functions you need.

### 7.2 `setwd()`
Be careful when using `setwd()`. Usage of the absolute path (like `"/Users/Alladin/Documents/sannic-project/files/"`) can limit reproducibility. It is the same about reading and writing files in a script (like `read.csv(file = "/Users/Alladin/Documents/sannic-project/files/dataset-2013-01.csv")`).

### 7.3 Temporary objects
For long codes it is a good practice to remove temporary objects after they have served their purpose. It will make it easear to debug the code.

---

## 8. Cautionary Tale

In 2017 Boeing released a new airplane Boeing 737 MAX. Its position of engines made the nose of planes go upward. To compensate for this, they implemented a computer program called [MCAS](https://en.wikipedia.org/wiki/Maneuvering_Characteristics_Augmentation_System) that lowered the nose automatically.

However, Boeing did not release the documentation for the program. Therefore, pilots didn't know that it even exists. It led to two major accidents
([here](https://en.wikipedia.org/wiki/Lion_Air_Flight_610) and
[here](https://en.wikipedia.org/wiki/Ethiopian_Airlines_Flight_302))
and Boeing 737 MAX was banned in multiple countries (including all the EU, Russia, US etc.).

And that's why you should provide documentation.
