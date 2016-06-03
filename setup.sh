# Install TextPlayer
git clone https://github.com/kingjamesiv/textplayer.git

# Install a modified fork of Frotz and build it specifically for interaction with the command line
cd textplayer/
git clone https://github.com/kingjamesiv/frotz.git
cd frotz/
make dumb
cd ../..

# Install Scholar
git clone https://github.com/kingjamesiv/scholar.git

# Install Conceptnetter
git clone https://github.com/kingjamesiv/conceptnetter.git

# Install NLTK and Word2Vec
pip install nltk
sudo apt-get -y install cython
sudo pip install word2vec
