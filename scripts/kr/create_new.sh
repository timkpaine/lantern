#!/bin/bash
if [[ $# -ne 2 ]]; then
    echo "usage: create_new.sh <repo_path> <notebook name>"
else
    knowledge_repo --repo $1 create ipynb posts/$2.ipynb
fi
