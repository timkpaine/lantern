#!/bin/bash
if [[ $# -ne 1 ]]; then
    echo "usage: deploy.sh <repo_path>"
else
    knowledge_repo --repo $1 deploy
    # knowledge_repo --repo $1 --repo $2 --repo $3 ...etc deploy
fi
