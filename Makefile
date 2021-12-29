
cat:
	cat Makefile

publish:
	cat ~/token.txt
	git add --all .
	git commit -m "AutoUpdate from Make tony - Jan-2022"
	git push


git-hell:
	echo 'git log and then git reset <commit> -- clear all output cells cntl-s -- make publish'
