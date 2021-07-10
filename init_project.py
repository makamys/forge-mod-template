from string import Template
import os
import sys
from pathlib import Path

props = dict([x.strip().split("=") for x in list(open("gradle.properties", "r", encoding="utf8")) if "=" in x])
props["package"] = props["group"]
props["mainclass"] = props["modid"].capitalize()

def apply_template(template_path, source_path_str):
    source = Template(open(template_path, "r", encoding="utf8").read()).substitute(props)

    source_path = Path(source_path_str)

    os.makedirs(source_path.parent, exist_ok=True)
    open(source_path, "w", encoding="utf8").write(source)
    
    os.remove(template_path)

apply_template("src/main/java/Template.java", "src/main/java/" + props["package"].replace(".", "/") + "/" + props["mainclass"] + ".java")
apply_template("src/main/resources/template.mixin.json", "src/main/resources/" + props["modid"] + ".mixin.json")

os.remove(sys.argv[0])
os.remove("README.md")