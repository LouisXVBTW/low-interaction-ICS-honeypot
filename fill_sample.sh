#!/bin/sh

for file in stage1/files/*; 
do 
    echo $file | grep -v "__";
    
done