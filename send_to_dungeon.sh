#!/bin/sh

DB="dnd_database"

DIR="/tmp/prisoners"
mkdir -p $DIR
FILE="prisoner_"`date "+%Y%m%d%H%M%S"`

TARGET="root@138.68.62.110"
TARGET_DIR="~/prisoners"

dokku postgresql:export $DB | gzip > $DIR/$FILE

scp $DIR/$FILE $TARGET:$TARGET_DIR

rm -rf $DIR
