git clone --mirror --depth=5  file://$PWD ../temp
rm -rf .git/objects
mv ../temp/{shallow,objects} .git
rm -rf ../temp
