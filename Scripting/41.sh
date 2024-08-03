#! /bin/bash

#Decision Making Test

read -p "Username: " USR
read -sp "Password: " PWD
echo

echo "Login Successfule, Welcome Dear "$USR" "
read -p "Your Age: " AG
echo

if [ $AG -gt 100 ]
then
echo "we re in a decision block"
sleep 3
echo " You are older than 100 years "
echo
date
else 
echo "You are younger than 100 years "
fi
