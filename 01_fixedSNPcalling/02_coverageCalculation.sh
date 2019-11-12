#!/bin/bash
# count the bases in the trimmed fastq.gz files.
# my_directory/list.txt contains the names for all the fastq.gz files.
LISTFILE="my_directory/list.txt"
while read FILE
do
	echo $FILE >>trim_count.txt
	zcat $FILE | paste - - - - | cut -f 2 | tr -d '\n' | wc -c >>trim_count.txt
done < $LISTFILE
