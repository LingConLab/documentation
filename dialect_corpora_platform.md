## Administration

To administrate your project on a hosting you can use either terminal (then you need to install **ssh** package) or FTP-client (e.g. PuTTY for Windows, FileZilla for Linux).

Access requiruments:

- **linghub.ru**: public key + passphrase, password

Make ssh connection via `ssh -i here/a/path/to/your/public/key username@linghub.ru`.

- **parasolcorpus.org**: password

Make ssh connection via `ssh username@parasolcorpus.org`.

---

## Setting corpus on server

- **linghub.ru**

1. create of a corpus folder in your user directory - that will be your project directory

2. go to the project directory and create two subdirectories for an interface (further - `/corpus_spoco`) and for a generator (further - `/corpus_data`). Place there files and folders that are privided in materials section

- **parasolcorpus.org**

1. go up to the root directory

2. in folder `аdditionaldisk` create a project directory and place there a generator provided in materials section 

3. return to the root directory and go into `/var/www/html/`. There you should create another project directory and place interface sources into it

In further documentation the difference of location of `/corpus_data` and `/corpus_spoco` directories in the hostings will not be mentioned. Nevertheless, you should keep it mind while editing paths, otherwise corpus generation may crash.

---

## Data preparation

**audio files**

1. audio file names must contain only latin letters, numbers and/or \_

2. recommended format is `.wav` written lowercase, e.g. a file name:

`20102018_mgd10.wav`

3. put audiofiles in `<...>/corpus_data/ENDVERSION` directory

**annotations**

1. annotations must be in `.eaf` forman (elan-file) or converted into it

2. names of annotation files must be identical to names of adudiofiles they are related to

3. into each elan-file (after `<HEADER MEDIA_FILE="" TIME_UNITS="milliseconds">` tag) you should manually place further line. Change **audio_file_name.wav** into a name of an audio-file that is related to the annotation:

> <MEDIA_DESCRIPTOR MEDIA_URL="" MIME_TYPE="audio/x-wav" RELATIVE_MEDIA_URL="./**audio_file_name.wav**"/>

4. if speech of interviewers is tagged too, make sure that the layer is named exactly as **Interviewer** or rename it if neccessary in every file

5. put edited elan-files to the `<...>/corpus_data/ELAN-FILES` directory

**metadata**

You should compile metadata of consultants who took part in audio recoding into `metadata_export.xml` file and put in into `/corpus_data` directory. The file must be structured like this:
```
<meta>
  <person>
    <tag1> ... </tag1>
    <tag2> ... </tag2>
           ...
  <person>
  <person>
    <tag1> ... </tag1>
    <tag2> ... </tag2>
           ...
  </person>
  ...
</meta>
```
One tag must refer to one section of metadata (e.g. year of birth, education, place of birth etc.). It is nice if tag name corresponds do its content, e.g. `<education>` tag contains information about education of a consultant.

You should choose 3-6 sections and create a short unification for them to use it for search. For example, you may shorten detailed information about education to "primary", "secondary", "higher" and etc. fields.

Insert tags that you have chosen for search into `metaTags` list in `add_meta.py` file like this:

`metaTags = ['id', 'string_id', 'sex', 'year_of_birth', 'education', 'russian_age']`

---

## Corpus generation

coming soon

---

## Interface editing

coming soon

---

## Materials

1. [Template corpus interface](https://bitbucket.org/michauw/spoco/src/master/)

2. [Template corpus generator](https://drive.google.com/open?id=1V3Wyq3LL7t7b5JxSCtRiOnJ_gYfD8TEz)
