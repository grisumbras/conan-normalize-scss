#!/bin/sh

old_ifs="$IFS"
IFS=:
for dir in $SASS_PATH; do
  if [ -n "$dir" ]; then
    includes="$includes${includes:+ }-I$dir"
  fi
done
eval sassc "$@" "$includes" >style.css
