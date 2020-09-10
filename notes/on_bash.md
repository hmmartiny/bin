# Notes on bash commands/scripts
**FYI**: Whenever <*string*> is written, replace it with your own variable name or pattern.

## Searching in directories
Finding specific file extensions:
```bash
find <dir> -type f -name "*.<extension>"
```
Alternative:
```bash
ls <dir>/*.<extension>
```

## Comparing items
Cutting out substrings to see if file substring is in another directory:
```bash
for x in <dir1>/<pattern>; do
    n=$(echo $x | cut -d'<delimiter>' -f<number> | cut ...)

    if [ -f <dir2>/$n<pattern> ]; then
        echo "File exists with substring $n"
    else
        echo "File does not exist with substring $n"
    fi
done
```
Example: See if expected output file were created by pattern matching input files
```bash
for x in <input_dir>/*.<in>; do

    ## cut out the path (so what comes before '/')
    n=$(echo $x | cut -d'/' -f2 ) 

    if [-f <output>/$n.<out> ]; then
        echo "output were created with $x as input"
    else
        echo "$x failed to create output"
    fi
done
```

## Creating bash scripts
### Inputting commands from command line
Let's say we have a script (example.sh) and want to give the directory from the command line:
```bash
#!/bin/bash

DIR=$1

for x in $DIR/*; do
    echo $x
done
```
then the directory is given as `$1`, so 
```
./example.sh output_dir
````
will loop through the files in output_dir.

### Inputting variables with qsub
Instead one can remove `DIR=$1`, if using qsub to submit a job, as variables can be given with `-v`:
```bash
qsub [options] -v DIR='dir' example.sh
```