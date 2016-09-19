# practiceRep
This is a test repository for group members to freely practice pulling, pushing, push/pull requests, and anything else they wish to do.
ALL MEMBERS ARE ENOURAGED TO CORRECT/ADD TO THIS README AND COMMENT ON WHAT YOU ARE DOING.

 - CLONING THE REPOSITORY TO YOUR LOCAL MACHINE:

 ~/Desktop$ git clone git@github.com:ub-cse442/practiceRep.git

 - CREATING A BRANCH ON YOUR LOCAL MACHINE:

~/Desktop/practiceRep$ git branch bens_branch

 - POINTING TO THE BRANCH ON YOUR LOCAL MACHINE:
 
~/Desktop$ git checkout bens_branch 

 - TELL GIT YOU WANT TO ADD A FILE TO YOUR LOCAL BRANCH 

~/Desktop$ git add bensfile
(I made a simple file called "bensfile." Make sure you are pointing to the correct branch when you do this command)

 - SUBMIT THE FILE TO YOUR LOCAL BRANCH

 ~/Desktop$ git commit -m "adding bensfile to bens_branch"
(if you have added many files with the git add <file> command, it will submit all of them at once unless you specify otherwise.)

- SUBMIT YOUR BRANCH WITH YOUR FILE IN IT TO REMOTE (Github)

 ~/Desktop$ git push origin bens_branch

