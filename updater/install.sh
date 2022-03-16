# Run this from the root dir of this repo to update the buildscript in another
# repo. It's highly recommended to clean the working and staging area before
# doing this, so you can correct the changes.
#
# $1: The directory of the repo to update

rsync -av . $1 --exclude-from='updater/excludes.txt'
rsync -av .github.disabled/* $1/.github