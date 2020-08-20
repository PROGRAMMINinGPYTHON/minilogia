#!/bin/bash

kod="bas"

for file in $kod/in/*in
do
  bname=$(basename $file)
#  echo $file
  solution="$kod/out/${bname%.*}.out"
#  echo "testing $file $solution"
#  echo $solution
  cat $file | python3 "$kod.py" > out.txt
  diff out.txt $solution &>/dev/null
  error=$?
#  echo "err " $error
  if [ $error -eq 0 ]
  then
     echo "OK $file"

  else
    echo "ERROR $file solution: $solution"
    exit
  fi
done

#cat "ser/in/ser0a.in"
#python3 "$kod.py" < "ser/in/ser0a.in" > out.txt