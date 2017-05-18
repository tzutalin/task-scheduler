#!/bin/sh
# $1 is path, $2 is branch, $3 is remote
echo "Usage PATH BRANCH REMOTE"
if [ -z "$1" ]; then
    echo "No src path"
    exit 1
fi

if [ -z "$2" ]; then
    echo "No branch"
    exit 1
fi

if [ -z "$3" ]; then
    echo "No remote"
    exit 1
fi

if [ ! -d "$1" ]; then
    echo "$1 does not exist"
    exit 1
fi

cd $1
git checkout $2
git reset --hard HEAD
git fetch --all
git reset --hard $3/$2
git rebase $3/$2
