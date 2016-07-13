# Run the following bash commands. Instead of "sudo pip install asciitree", you may need to run "sudo -H pip install asciitree" instead

# Install JDK8
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get -y update
sudo apt-get -y install oracle-java8-installer

# Install miscellaneous
sudo apt-get -y install pkg-config zip g++ zlib1g-dev unzip

# Download and install Bazel
wget https://github.com/bazelbuild/bazel/releases/download/0.2.2b/bazel-0.2.2b-installer-linux-x86_64.sh
chmod +x bazel-0.2.2b-installer-linux-x86_64.sh
./bazel-0.2.2b-installer-linux-x86_64.sh --user

# Set up environment variables
export PATH="$PATH:$HOME/bin"

# Install Swig
sudo apt-get -y install swig

# Install protobuf (Requires Pip)
sudo apt-get -y install python-pip
sudo pip install -U protobuf==3.0.0b2

# Install asciitree
sudo pip install asciitree

# Install numpy (Requires python-dev)
sudo apt-get -y install python-dev
sudo pip install numpy

# Download and install Tensorflow & Syntaxnet (Requires git)
sudo apt-get -y install git
git clone --recursive https://github.com/tensorflow/models.git
cd models/syntaxnet/tensorflow
./configure
cd ..
bazel test syntaxnet/... util/utf8/...

# Create a folder in autoplay/ called parsey/
# Now copy the contents of models/syntaxnet/ into autoplay/parsey/
# Run setup_parsey.sh
