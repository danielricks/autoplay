
# autoplay: a learning environment for interactive fiction

Autoplay is a learning environment for creating agents that play text-based games. Supported games include the popular Zork series and other z-machine interpretable files (specifically the .z5 format). These games are provided as part of this repository.

This repository uses a modified fork of [Frotz](https://github.com/DavidGriffith/frotz), a z-machine interpreter maintained by David Griffith. A [python interface](https://github.com/danielricks/textplayer) for Frotz is included as well, which allows games to be run in parallel and controlled using python.

By default, several independent repositories are cloned during setup to create this environment. Generally an agent will require the ability to part-of-speech tag text, so the Natural Language Toolkit [(NLTK)](http://www.nltk.org/) is installed. We found [word2vec](https://code.google.com/archive/p/word2vec/) to be a valuable tool, so an [interface](https://github.com/danielricks/scholar) for that is installed as well.

A note: our interface for word2vec uses a part-of-speech tagged corpus, so it cannot be swapped out with a normal word2vec .bin file. The corpus used is a copy of Wikipedia from January 2016.

## Setup

I. The following script will install Frotz, textplayer (Frotz interface), NLTK, word2vec, and scholar (word2Vec interface) in the autoplay folder.

```bash
$ chmod +x setup.sh
$ ./setup.sh
```

II. Download a copy of the [scholar dependencies](https://drive.google.com/file/d/1srOUFidQ9fV240wyF7GW4eqF6raCawBV/view), extract, and move the files to autoplay/scholar. See the [scholar Github page](https://github.com/danielricks/scholar) for more information on use.

## Agents

A number of agents are included with this code. The agents included are: a basic navigational agent and a more sophisticated noun-verb processing agent.

We won the IEEE CIG 2016 Text-based Adventure Competition! Our autoplay-compatible agent is provided [here](https://github.com/danielricks/BYU-Agent-2016).

## Usage

### Automated

Running the main file will run a number of agents on separate processes. The example below will run 5 agents on Zork I.

```bash
$ python autoplay.py zork1.z5 5
```

Running the code without at least two additional parameters will result in the available games being displayed.

```bash
$ python autoplay.py zork1.z5
Needs more parameters. Try 'python autoplay.py zork1.z5 5'.
Current games include:  Advent.z5 Adventureland.z5 Balances.z5 BrandX.z5 ...
```

### Human

There are two ways to play the games, either to get more intuition about the formatting of the text, or for fun.

From the autoplay folder (text reformatted for agents):
```bash
$ python play.py zork1.z5
```

From the textplayer folder (direct interface with Frotz):
```bash
$ frotz/dfrotz games/zork1.z5
```
