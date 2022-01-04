. ..\utils\make-exercise-repo.ps1

Set-Content -Value "" -Path greeting.txt
cd exercise
git add greeting.txt
git commit -m "Add file greeting.txt"

Set-Content -Value "hello" -Path greeting.txt

git add greeting.txt
git commit -m "Add content to greeting.txt"

cd ..

# Create a file on branch1
git branch merge-conflict-branch1
git checkout merge-conflict-branch1

Set-Content -Value "This is a relevant fact" -Path file.txt

git add file.txt
git commit -m "add relevant fact"

git checkout master

Set-Content -Value "This is an indispensable truth!" -Path file.txt

git add file.txt
git commit -m "add indispensable truth!"
