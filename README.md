
# autoplay: a learning environment for interactive fiction

Autoplay is a learning environment for creating agents that play text-based games. Supported games include Zork I-III and other z-machine interpretable files (.z5). These games are provided as part of this repository.

This repository uses a modified fork of [Frotz](https://github.com/DavidGriffith/frotz), a z-machine interpreter written by David Griffith. A [python interface](https://github.com/kingjamesiv/textplayer) for Frotz is included as well, which allows games to be run in parallel and controlled using python.

By default, several independent repositories are pulled during setup to create this environment. Generally an agent will require the ability to part-of-speech tag text, so the Natural Language Toolkit [(NLTK)](http://www.nltk.org/) is installed. We found [Word2vec](https://code.google.com/archive/p/word2vec/) to be a valuable tool, so an [interface](https://github.com/kingjamesiv/scholar) for that is installed as well.

## Setup

I. The following script will install Frotz, textplayer (Frotz interface), NLTK, Word2vec, and scholar (Word2Vec interface) in the autoplay folder.

```bash
$ chmod +x setup.sh
$ ./setup.sh
```

II. Move a copy of wikipedia_articles.bin and the text file to autoplay/scholar.

## Agents

A number of agents are included, but you are encouraged to create your own.

## Usage

Running the following code will run a number of agents on separate processes.

```python
python autoplay.py
```
