#!/bin/bash
if [[ $# -ne 2 ]]; then
    echo "usage: init_repo.sh <repo_path> <remote_url>"
else
    pwd=`pwd`
    knowledge_repo --repo $1 init
    cd $1
    git remote add origin $2
    git push -u origin master
    cd $pwd
fi

