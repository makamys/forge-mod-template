from string import Template
import os
import sys
from pathlib import Path

props = dict([x.strip().split("=") for x in list(open("gradle.properties", "r", encoding="utf8")) if "=" in x])
props["package"] = props["group"]
props["mainclass"] = props["modid"].capitalize()

template_path = "src/main/java/Template.java"
source = Template(open(template_path, "r", encoding="utf8").read()).substitute(props)

source_path = Path("src/main/java/" + props["package"].replace(".", "/") + "/" + props["mainclass"] + ".java")

os.makedirs(source_path.parent, exist_ok=True)
open(source_path, "w", encoding="utf8").write(source)

os.remove(template_path)
os.remove(sys.argv[0])