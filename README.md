
# autoplay

Main project files for teaching computers how to play text-based games

## Setup

I. The following script will install [textplayer](https://github.com/kingjamesiv/textplayer) (Frotz interface), [scholar](https://github.com/kingjamesiv/scholar) (Word2Vec interface), and [conceptnetter](https://github.com/kingjamesiv/conceptnetter) (ConceptNet 5 interface) in the autoplay folder.

```bash
$ chmod +x setup.sh
$ ./setup.sh
```

II. Move a copy of wikipedia_articles.bin to autoplay/scholar.

III. Move a copy of english_assertions.csv into autoplay/conceptnetter.
Or perform both the bash and python code below.

```bash
$ wget http://conceptnet5.media.mit.edu/downloads/current/conceptnet5_flat_csv_5.4.tar.bz2
$ mv data conceptnetter
```
And now run the following commands in Python from the autoplay folder.
```python
import conceptnetter.conceptNetter as cn
c = cn.ConceptNetter()
c.create_english_CSV_file()
```

IV. Install [Parsey McParseface](https://github.com/tensorflow/models/tree/master/syntaxnet). If Parsey is already installed, continue to step V. This script should not be run in autoplay/, and is recommended to be run in Downloads/. It requires root access, Ubuntu 14.04, and Python 2.7.

```bash
$ chmod +x install_parsey.sh
$ ./install_parsey.sh
```

V. Create parsey/ in autoplay/. Move the contents of model/syntaxnet into autoplay/parsey. Then run the following script.

```bash
$ chmod +x setup_parsey.sh
$ ./setup_parsey.sh
```

## Usage

Running the following code will run a number of agents on separate processes.

```python
python autoplay.py
```
