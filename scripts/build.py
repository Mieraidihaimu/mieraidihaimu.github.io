"""Render portfolio data into static HTML. Run: python3 scripts/build.py."""
import json
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def text(value):
    return escape(value, quote=True)


def link(url, label, class_name=""):
    if not url.startswith("https://"):
        raise ValueError(f"Expected an HTTPS project or thesis URL: {url}")
    return (f'<a href="{text(url)}" class="{class_name}" target="_blank" '
            f'rel="noopener noreferrer">{text(label)} <span aria-hidden="true">↗</span></a>')


def experience(item):
    details = ""
    if item["details"]:
        points = "".join(f'<li>{text(point)}</li>' for point in item["details"])
        details = f'''<details class="technical-details">
          <summary>Technical details</summary>
          <ul>{points}</ul>
          <p class="stack">{text(item["stack"])}</p>
        </details>'''
    return f'''<article class="experience-item" id="{text(item["id"])}">
        <p class="experience-date">{text(item["year"])}</p>
        <div>
          <div class="job-heading"><h3>{text(item["company"])}</h3><span class="location">{text(item["location"])}</span></div>
          <p class="role">{text(item["role"])}</p>
          <p class="job-summary">{text(item["summary"])}</p>
          {details}
        </div>
      </article>'''


def earlier(item):
    source = link(item["link"], item["linkLabel"], "thesis-link") if item.get("link") else ""
    return f'''<article class="earlier-item" id="{text(item["id"])}">
            <p class="experience-date">{text(item["year"])}</p>
            <h3>{text(item["company"])}</h3>
            <p>{text(item["summary"])}</p>
            {source}
          </article>'''


def project(item):
    return f'''<article class="project" id="project-{text(item["id"])}">
          <span class="project-category">{text(item["category"])}</span>
          <h3>{text(item["name"])}</h3>
          <p>{text(item["summary"])}</p>
          {link(item["url"], item["linkLabel"])}
        </article>'''


def experiment(item):
    name = (link(item["url"], item["name"]) if item.get("url")
            else f'<strong>{text(item["name"])}<span class="experiment-label">{text(item["category"])}</span></strong>')
    return f'<li id="project-{text(item["id"])}"><div>{name}</div><p>{text(item["summary"])}</p></li>'


def build():
    data = json.loads((ROOT / "data/timeline.json").read_text(encoding="utf-8"))
    sections = {
        "EXPERIENCE": "\n      ".join(map(experience, data["milestones"])),
        "EARLIER": "\n          ".join(map(earlier, data["earlier"])),
        "PROJECTS": "\n        ".join(project(item) for item in data["projects"] if item["featured"]),
        "EXPERIMENTS": "\n          ".join(experiment(item) for item in data["projects"] if not item["featured"]),
    }
    path = ROOT / "index.html"
    html = path.read_text(encoding="utf-8")
    for section, content in sections.items():
        pattern = rf'(<!-- BEGIN {section} -->).*?(<!-- END {section} -->)'
        html, count = re.subn(pattern, lambda match: f'{match[1]}\n      {content}\n      {match[2]}', html, flags=re.S)
        if count != 1:
            raise ValueError(f"Expected one {section} region, found {count}")
    path.write_text(html, encoding="utf-8")
    print("Built index.html from data/timeline.json")


if __name__ == "__main__":
    build()
