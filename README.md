
# autoplay: a learning environment for interactive fiction

Autoplay is a learning environment for creating agents that play text-based games. Supported games include the popular Zork series and other z-machine interpretable files (specifically the .z5 format). These games are provided as part of this repository.

This repository uses a modified fork of [Frotz](https://github.com/DavidGriffith/frotz), a z-machine interpreter written by David Griffith. A [python interface](https://github.com/kingjamesiv/textplayer) for Frotz is included as well, which allows games to be run in parallel and controlled using python.

By default, several independent repositories are cloned during setup to create this environment. Generally an agent will require the ability to part-of-speech tag text, so the Natural Language Toolkit [(NLTK)](http://www.nltk.org/) is installed. We found [Word2vec](https://code.google.com/archive/p/word2vec/) to be a valuable tool, so an [interface](https://github.com/kingjamesiv/scholar) for that is installed as well.

A note: our interface for Word2vec uses a part-of-speech tagged corpus, so it cannot be swapped out. The corpus used is a copy of Wikipedia from January 2016.

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

Running the following code will run a number of agents on separate processes. The example below will run 5 agents on Zork I.

```python
python autoplay.py zork1.z5 5
```

Running the code without at least two additional parameters will result in the available games being displayed.

```python
python autoplay.py
Needs more parameters. Try 'python autoplay.py zork1.z5 5'.
Current games include:  Advent.z5 Adventureland.z5 Balances.z5 BrandX.z5 Murdac.z5 Parc.z5 acorncourt.z5 amish.z5 awaken.z5 break-in.z5 building.z5 bunny.z5 candy.z5 causality.z5 cavetrip.z5 cheater.z5 cia.z5 curses.z5 death.z5 deephome.z5 detective.z5 enter.z5 fable.z5 frozen.z5 gold.z5 inhumane.z5 jewel.z5 karn.z5 library.z5 lily.z5 loose.z5 mansion.z5 minster.z5 night.z5 omniquest.z5 parallel.z5 pentari.z5 piracy_2.z5 reverb.z5 sherbet.z5 spirit.z5 spot.z5 temple.z5 theatre.z5 tryst205.z5 zenon.z5 zork1.z5 zork2.z5 zork3.z5 ztuu.z5
```
