#!/bin/bash
if [[ $# -ne 1 ]]; then
    echo "usage: runserver.sh <repo_path>"
else
    knowledge_repo --repo $1 runserver
    # knowledge_repo --repo $1 --repo $2 --repo $3 ...etc riunserver
fi
