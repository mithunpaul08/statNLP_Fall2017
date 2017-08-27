
if [ -z "$1"]
then
echo "No argument supplied"
fi

git add --all
git commit -m "will print top 10 most frequent lemmas"
git push origin master
