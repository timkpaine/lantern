#!/bin/bash
if [[ $# -ne 2 ]]; then
    echo "usage: submit.sh <repo_path> <notebook name>"
else
    knowledge_repo --repo $1 submit posts/$2.ipynb.kp
    git checkout master
    git merge posts/$2.ipynb.kp
fi
