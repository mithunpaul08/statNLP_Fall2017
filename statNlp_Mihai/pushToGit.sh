#!/usr/bin/env bash

comment="my default comment"


if [ -z "$1" ];
then
	echo "No argument supplied"
	else
	comment="$1"
fi

branch="master"


 
if [ -z "$2" ];
 then    
              echo "No branch supplied"
                 else
	          branch= "$2"
		 
	  fi


git add --all
git commit -m "$comment"
git push origin $branch





