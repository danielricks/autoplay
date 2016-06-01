
# autoplay

Main project files for teaching computers how to play text-based games

## Setup

The following script will install [textplayer](https://github.com/kingjamesiv/textplayer) (Frotz interface), [scholar](https://github.com/kingjamesiv/scholar) (Word2Vec interface), and [conceptnetter](https://github.com/kingjamesiv/conceptnetter) (ConceptNet 5 interface) in the autoplay folder.

```bash
$ ./setup.sh
```

Move a copy of wikipedia_articles.bin to autoplay/scholar.

Move a copy of english_assertions.csv into autoplay/conceptnetter.
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

## Usage

Running the following code will run a number of agents on separate processes.

```python
python autoplay.py
```
