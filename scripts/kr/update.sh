#!/bin/bash
if [[ $# -ne 2 ]]; then
    echo "usage: update.sh <repo_path> <notebook name>"
else
    knowledge_repo --repo $1 add --update posts/$2.ipynb  -p posts/$2.ipynb
fi
