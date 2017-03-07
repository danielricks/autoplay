
# autoplay
## An interactive fiction learning environment

Main project files for teaching computers how to play text-based games

## Setup

I. The following script will install [textplayer](https://github.com/kingjamesiv/textplayer) (Frotz interface), [scholar](https://github.com/kingjamesiv/scholar) (Word2Vec interface), and [penseur](https://github.com/kingjamesiv/penseur) (skip-thoughts interface) in the autoplay folder.

```bash
$ chmod +x setup.sh
$ ./setup.sh
```

II. Move a copy of wikipedia_articles.bin to autoplay/scholar.

## Usage

Running the following code will run a number of agents on separate processes.

```python
python autoplay.py
```
