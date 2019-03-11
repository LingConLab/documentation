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

1. set proper base_path to `/corpus_spoco` in `add_meta.py` according to hosting you use

2. sit proper paths to `/corpus_data` and `/corpus_spoco` in files `/corpus_data/REBUILDCORPUSnoSoundfilesRolling.sh` and `/corpus_spoco/settings/init.php`

3. create symbolic links of `/corpus_data/FullTexts.html` and `/corpus_data/files_html` with the same names into `/corpus_spoco`

4. if `/corpus_data` run `sh REBUILDCORPUSnoSoundfilesRolling.sh` via command line (you should make ssh connection fot that, check out **administration** section) and wait finishing of corpus generation

After that, the following functions must be accessible on your project site:

- search with the use of metadata and grammar tags

- audio fragments in a search output

- extended context in search output

- valid list of full texts

- list of lexems and wordforms

If something of that is not accessible, perhaps you have made a mistake in previous steps. To find out the problem it is useful to run rebuild script again (p. 4) and **read its log carefull - it will warn you about the cause of a crash**.

---

## Interface editing

1. change a title name of your project in `/corpus_spoco/index.php` and in `/corpus_spoco/jsapp/corpus.js` everywhere you see

2. 

---

## Materials

1. [Template corpus interface](https://bitbucket.org/michauw/spoco/src/master/)

2. [Template corpus generator](https://drive.google.com/open?id=1V3Wyq3LL7t7b5JxSCtRiOnJ_gYfD8TEz)
