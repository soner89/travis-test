git config --global user.email "travis@travis-ci.org"
git config --global user.name  "Travis CI"

git checkout master
git add .
git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"

git remote add origin https://${GH_TOKEN}@github.com/soner89/travis-test > /dev/null 2>&1
git push --quiet --set-upstream origin master
