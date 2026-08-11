from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
failures: list[str] = []


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        failures.append(message)


config = read("_config.yml")
about = read("_pages/about.md")
navigation = read("_data/navigation.yml")

require(re.search(r'^url\s*:\s*"?https://hunter-summer\.github\.io"?\s*$', config, re.M) is not None,
        "_config.yml must use the GitHub Pages host as url")
require(re.search(r'^baseurl\s*:\s*"/yongranzhi\.github\.io"\s*$', config, re.M) is not None,
        "_config.yml must use /yongranzhi.github.io as baseurl")
require(re.search(r'^\s*github\s*:\s*"Hunter-summer"\s*$', config, re.M) is not None,
        "author.github must be Hunter-summer")
require("sunshine boy" not in config.lower(), "template biography must be removed")
require('title: "Guide"' not in navigation, "Guide must be removed from primary navigation")
require("]([" not in about, "homepage contains malformed nested Markdown links")
require("Google Scholar" in about and "ORCID" in about and "Publications" in about,
        "homepage must link to core academic profiles and publications")

collection_files = list((ROOT / "_publications").glob("*.md"))
collection_files += list((ROOT / "_talks").glob("*.md"))
collection_files += list((ROOT / "_teaching").glob("*.md"))

permalink_owners: dict[str, Path] = {}
for path in collection_files:
    text = path.read_text(encoding="utf-8")
    require(text.startswith("---\n") or text.startswith("---\r\n"),
            f"{path.relative_to(ROOT)} must start with YAML front matter")
    require(text.count("---") >= 2, f"{path.relative_to(ROOT)} has incomplete front matter")
    require("鈥" not in text, f"{path.relative_to(ROOT)} contains mojibake")
    title_match = re.search(r'^title:\s*(["\'])(.*?)\1\s*$', text, re.M)
    require(title_match is not None, f"{path.relative_to(ROOT)} has an invalid quoted title")
    permalink_match = re.search(r'^permalink:\s*(\S+)\s*$', text, re.M)
    if permalink_match:
        permalink = permalink_match.group(1)
        if permalink in permalink_owners:
            failures.append(
                f"duplicate permalink {permalink}: {permalink_owners[permalink].relative_to(ROOT)} and {path.relative_to(ROOT)}"
            )
        else:
            permalink_owners[permalink] = path

if failures:
    print("Academic site validation failed:")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print(f"Academic site validation passed ({len(collection_files)} collection files checked).")
