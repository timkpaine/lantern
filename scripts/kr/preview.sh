#!/bin/bash
if [[ $# -ne 2 ]]; then
    echo "usage: preview.sh <repo_path> <notebook name>"
else
    knowledge_repo --repo $1 preview posts/$2.ipynb.kp
fi
