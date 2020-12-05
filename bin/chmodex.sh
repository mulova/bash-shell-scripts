find . -type d -exec chmod $1 {} \;
find . -type f -exec chmod $2 {} \;
