# Forge 1.7.10 example project

This is an example mod using the [fork of ForgeGradle-1.2 made by anatawa12](https://github.com/anatawa12/ForgeGradle-1.2), which supports Gradle 4.4.1 and later. This example project uses Gradle 6.4. It can be used as a replacement for Forge's 1.7.10 MDK.

## How to use this example project

1. Clone the repo
```
git clone --single-branch --branch 1.7.10 https://github.com/makamys/forge-example-mod
cd forge-example-mod
```
2. Edit the metadata (mod ID, etc.) in `gradle.properties`
3. Run `py init_project.py` to generate the project files. This script automatically substitutes your metadata into the source files, and deletes itself once it's done.
4. Run `./gradlew setupDecompWorkspace eclipse` (you can use `idea` instead of `eclipse`)
5. Now you can open the project in your IDE. Don't forget to edit the mod info in `mcmod.info`. Happy coding!

### Running in Eclipse
ForgeGradle 1.2 doesn't generate launch configurations for Eclipse. To get them, copy the launch configuration of another mod and correct the paths in them. If this is the first mod in your workspace, you can use the 1.12.2 MDK's project as the seed. Download it, run `gradlew eclipse`, and copy the generated `.launch` files into your project. It's convoluted, but it's the best way I know.

### Tips

* CodeChickenLib is included in the dependencies, so you can get other non-deobfuscated mods running in your dev environment by putting them either in the `libs` directory you create inside this one (you'll have to run `./gradlew eclipse` (or `idea`)  again whenever you change that directory), or in the `mods` folder of your instance.
* Once you're done, build your project with `./gradlew build`.