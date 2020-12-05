#! /bin/sh

echo "Purging pyc files and empty directories..."

# Start from the repository root.
cd ./$(git rev-parse --show-cdup)

# Delete .pyc files
find . -name "*.pyc" -delete 2>&1 > /dev/null &

# Delete empty directories.
 
while [ -n "$(find ./Assets -type d -empty)" ]
do
    echo "Found empty directories... removing...";
    find ./Assets -type d -empty -exec rm -rf {}.meta \;
    find ./Assets -type d -empty -exec rm -rf {} \; &> /dev/null
done
