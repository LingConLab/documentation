## Administration

To administrate your project on a hosting you can use either terminal (then you need to install **ssh** package) or FTP-client (e.g. PuTTY for Windows, FileZilla for Linux).

Access requiruments:

- **linghub.ru**: public key + passphrase, password

Make ssh connection via `ssh -i here/a/path/to/your/public/key username@linghub.ru`.

- **parasolcorpus.org**: user having access to root directories, password

Make ssh connection via `ssh username@parasolcorpus.org`.

---

## Setting corpus on server

- **linghub.ru**

1. create a corpus folder in your user directory - that will be your project directory

2. go to the project directory and create subdirectories for an interface (further it will be named `/corpus_spoco`) and for a generator (further - `/corpus_data`). Place there files and folders that are provided in materials section

- **parasolcorpus.org**

1. go up to the root directory

2. in folder `аdditionaldisk` create a project directory and place there a generator (further it will be named  `/corpus_data`) provided in materials section 

3. return to the root directory and go into `/var/www/html/`. There you should create another project directory (further - `/corpus_spoco`) and place interface sources into it

In further documentation the difference of location of `/corpus_data` and `/corpus_spoco` directories in the hostings will not be mentioned. Nevertheless, you should keep it mind while editing paths, otherwise **corpus generation may crash**.

---

## Data preparation

**audio files**

1. audio file names must contain only latin letters, numbers and/or \_

2. recommended format is `.wav` written lowercase, e.g. a file name:

`20102018_mgd10.wav`

3. put audio files in `<...>/corpus_data/ENDVERSION` directory

**annotations**

1. annotations must be in `.eaf` forman (elan-file) or converted into it

2. names of annotation files **must be identical** to names of audio files they are related to

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

Also set the same tags in `/corpus_spoco/settings/meta.json` file as in a template example, in `/corpus_spoco/backend/get_results.php` and in `/corpus_data/REBUILDCORPUSnoSoundfilesRolling.sh` (lines starting with `cwb-encode`).

If needed, change the number and positions of green buttons with meta tags in `corpus_spoco/jsapp/languageQuery/languageQuery.html` and `corpus_spoco/jsapp/languageQuery/languageQuery.js`.

---

## Corpus generation

1. set proper base_path to `/corpus_spoco` in `add_meta.py` and `annotator.py` according to hosting you use

2. set proper paths to `/corpus_data` and `/corpus_spoco` in files `/corpus_data/REBUILDCORPUSnoSoundfilesRolling.sh` and `/corpus_spoco/settings/init.php`

3. create symbolic links of `/corpus_data/FullTexts.html` and `/corpus_data/files_html` with the same names into `/corpus_spoco` (in the new version of the platform they are created automatically in `sh REBUILDCORPUSnoSoundfilesRolling.sh`)

4. in `/corpus_data` run `sh REBUILDCORPUSnoSoundfilesRolling.sh` via command line (you should make ssh connection for that and use a command line, check out **administration** section) and wait finishing of corpus generation

After that, the following functions must be accessible on your project site:

- search with the use of metadata and grammar tags

- audio fragments in a search output

- extended context in search output

- valid list of full texts

- list of lexems and wordforms

If something of that is not accessible, perhaps you have made a mistake in previous steps. To find out the problem it is useful to run rebuild script again (p. 4) and **read its log carefully for the cause of a crash**.

---

## Interface editing

Keep in mind, that sometimes changes that you make in the site interface cannot be browsed because of cash that your browser upload to save traffic instead of reloading page every time you press `f5`. So, you need clean cash of your project site to see the changes. For example, you can try [this solution](http://woocomp.ru/google-shrome-ochistka-kesha-otdelnogo-sajta-i-polnaya) (for Chrome). You need to do this every time you want fully reload your site.

1. change a title name of your project in `/corpus_spoco/index.php` and in `/corpus_spoco/jsapp/corpus.js` everywhere you see

2. upload a picture for background to `/corpus_spoco/images` and change the picture name in `/corpus_spoco/styl.less` (in the new version of the platform - in `/corpus_spoco/jsapp/pages/main.html`)

3. fill site sections with the project infornation in `/corpus_spoco/jsapp/info`

**It would be nice, if you cited _Rupreht von Waldenfels_ in a _"Project Team"_ section as the one who has taken part in technical solution of your project.**

4. update `/corpus_spoco/js/traslations.js` with transtations on Russian or other languages. Make sure, that all tags, which contents you would like to translate, are supplied with _transtale_ mathod, for instance:

`<p translate>Some text</p>`

Add the translation to `/corpus_spoco/js/traslations.js` as

> "Some text": "Some transtaled text"

Keep in mind that you must shield specific characters inside the text with `\`. If some text is not translated though you added it to the file, make sure that source text in the file is **identical** to the one you have inside translated tag and all spaces and characters are presist. If nothing is translated at all, you probably have syntax error in `/corpus_spoco/js/traslations.js`.

---

## Materials

1. [Template corpus interface](https://bitbucket.org/michauw/spoco/src/master/)

2. [Template corpus generator](https://drive.google.com/open?id=1V3Wyq3LL7t7b5JxSCtRiOnJ_gYfD8TEz)

---

### Contacts (for all questions)

Anastasia Panova *anastasia.b.panova[at]gmail[dot]com*

Lera Morozova *tito_alba[at]mail[dot]ru*
