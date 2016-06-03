
# autoplay

Main project files for teaching computers how to play text-based games

## Setup

I. The following script will install [textplayer](https://github.com/kingjamesiv/textplayer) (Frotz interface), [scholar](https://github.com/kingjamesiv/scholar) (Word2Vec interface), and [conceptnetter](https://github.com/kingjamesiv/conceptnetter) (ConceptNet 5 interface) in the autoplay folder.

```bash
$ chmod 555 setup.sh
$ ./setup.sh
```

II. Move a copy of wikipedia_articles.bin to autoplay/scholar.

III. Move a copy of english_assertions.csv into autoplay/conceptnetter.
Or perform both the bash and python code below.

```bash
$ wget http://conceptnet5.media.mit.edu/downloads/current/conceptnet5_flat_csv_5.4.tar.bz2
$ mv data conceptnetter
```
And now run the following commands from the autoplay folder.
```python
import conceptnetter.conceptNetter as cn
c = cn.ConceptNetter()
c.create_english_CSV_file()
```

IV. Create parsey/ in autoplay/. After installing [Parsey McParseface](https://github.com/tensorflow/models/tree/master/syntaxnet), move the contents of model/syntaxnet into autoplay/parsey. Then run the following script.

```bash
$ chmod 555 setup_parsey.sh
$ ./setup_parsey.sh
```

## Usage

Running the following code will run a number of agents on separate processes.

```python
python autoplay.py
```
