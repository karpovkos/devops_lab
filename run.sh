#! /bin/bash

#--- Check Centos distr
DISTRO=$( cat /etc/*-release | tr [:upper:] [:lower:] | grep -Poi '(debian|ubuntu|red hat|centos|nameyourdistro)' | uniq )
if [ -z $DISTRO ]; then
    DISTRO='unknown'
fi
echo "=============Detected Linux distribution: $DISTRO"
if [[ $DISTRO -ne "centos" ]]; then
    echo "=============WARNING: CentOS only installation!============="
    echo "=============Exit installation============="
    exit 1
fi

echo "=============Installation pyenv started============="

sudo yum install -y -q curl gcc gcc-c++ make git patch openssl-devel \
    zlib-devel readline-devel sqlite-devel bzip2-devel

curl -L https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

source ~/.bashrc

pyth_27="2.7.13"
pyth_38="3.8.3"

echo "=============Installation python ${pyth_27} started============="
pyenv install $pyth_27

echo "=============Installation python ${pyth_38} started============="
pyenv install $pyth_38

pyenv virtualenv $pyth_27 prod_pyth_27
pyenv virtualenv $pyth_38 prod_pyth_38
