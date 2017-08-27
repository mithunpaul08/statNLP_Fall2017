#!/usr/bin/env bash

comment="my default comment"
if [ -z "$1" ];
then
	echo "No argument supplied"
else
	comment="$1"
fi

echo $comment

git add --all
git commit -m $comment
git push origin master
