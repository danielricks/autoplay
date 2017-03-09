
# autoplay: a learning environment for interactive fiction

Autoplay is a learning environment for creating agents that play text-based games. Supported games include the popular Zork series and other z-machine interpretable files (specifically the .z5 format). These games are provided as part of this repository.

This repository uses a modified fork of [Frotz](https://github.com/DavidGriffith/frotz), a z-machine interpreter written by David Griffith. A [python interface](https://github.com/danielricks/textplayer) for Frotz is included as well, which allows games to be run in parallel and controlled using python.

By default, several independent repositories are cloned during setup to create this environment. Generally an agent will require the ability to part-of-speech tag text, so the Natural Language Toolkit [(NLTK)](http://www.nltk.org/) is installed. We found [Word2vec](https://code.google.com/archive/p/word2vec/) to be a valuable tool, so an [interface](https://github.com/danielricks/scholar) for that is installed as well.

A note: our interface for Word2vec uses a part-of-speech tagged corpus, so it cannot be swapped out. The corpus used is a copy of Wikipedia from January 2016.

## Setup

I. The following script will install Frotz, textplayer (Frotz interface), NLTK, Word2vec, and scholar (Word2Vec interface) in the autoplay folder.

```bash
$ chmod +x setup.sh
$ ./setup.sh
```

II. Move a copy of wikipedia_articles.bin and the text file to autoplay/scholar.

## Agents

A number of agents are included with this code. The agents included are: a basic navigational agent, a more sophisticated noun-verb processing agent, a Q-learning agent with affordance capabilities.

## Usage

Running the main file will run a number of agents on separate processes. The example below will run 5 agents on Zork I.

```python
python autoplay.py zork1.z5 5
```

Running the code without at least two additional parameters will result in the available games being displayed.

```python
python autoplay.py
Needs more parameters. Try 'python autoplay.py zork1.z5 5'.
Current games include:  Advent.z5 Adventureland.z5 Balances.z5 BrandX.z5 ...
```
