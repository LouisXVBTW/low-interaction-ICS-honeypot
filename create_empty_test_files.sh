#!/bin/sh

for file in stage1/files/protocols/*; 
do echo $file |
	cut -d "/" -f 4 | 
	grep -v "__" | 
	sed -e 's/^/test_/' >> files.txt; 
done; 
while read line; 
do touch stage1/files/$line; 
done < files.txt; 
rm files.txt
