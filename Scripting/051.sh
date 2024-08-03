#! /bin/bash
myuser="alpha beta gamma"

for usr in $myuser
do
	echo "Adding user $usr"
	useradd $usr
	id $usr
	echo "###"
done
