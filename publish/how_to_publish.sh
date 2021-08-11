# how 2 publish

# whenever a new game version is added
py ./prepare_publish.py

# to build the release
./gradlew cleanBuild

# to release
./gradlew githubRelease -PgithubToken=$GITHUB_TOKEN
py update_updatejson.py
./curseforge_all.sh -PcurseToken=$CURSEFORGE_TOKEN
#./modrinth_all.sh -PmodrinthToken=$MODRINTH_TOKEN