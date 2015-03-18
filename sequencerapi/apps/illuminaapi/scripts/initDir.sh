#!/bin/sh
echo `pwd`
source_dir=$1
dest_dir=$2
if [ ! -d $source_dir ];then
	mkdir $source_dir
fi
cd $source_dir
echo `pwd`
ln -s $dest_dir/* .
cp ./RunInfo.xml RunInfo_original.xml
rm -f RunInfo.xml
mv RunInfo_original.xml RunInfo.xml
