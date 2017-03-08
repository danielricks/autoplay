
# Install TextPlayer
git clone https://github.com/danielricks/textplayer.git

# Install a modified fork of Frotz and build it specifically for interaction with the command line
cd textplayer/
git clone https://github.com/danielricks/frotz.git
cd frotz/
make dumb
cd ../..

# Install NLTK and Word2Vec (Requires pip)
sudo apt-get -y install pip
sudo pip install nltk

# Install Word2vec
sudo apt-get -y install cython
sudo pip install word2vec

# Install Scholar
git clone https://github.com/danielricks/scholar.git
