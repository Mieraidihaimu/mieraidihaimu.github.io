"""Render portfolio data into static HTML. Run: python3 scripts/build.py."""
import json
import re
from html import escape
from pathlib import Path
from textwrap import indent

ROOT = Path(__file__).resolve().parent.parent


def text(value):
    return escape(value, quote=True)


def link(url, label):
    if not url.startswith("https://"):
        raise ValueError(f"Expected an HTTPS project or thesis URL: {url}")
    return f'<a href="{text(url)}">{text(label)}</a>'


def experience(item):
    row = [
        f'<article id="{text(item["id"])}">',
        f'  <h3>{text(item["company"])}</h3>',
        f'  <p class="entry-meta">{text(item["role"])} · {text(item["location"])} · {text(item["year"])}</p>',
        f'  <p>{text(item["summary"])}</p>',
    ]
    if item["details"]:
        row.extend(['  <details>', '    <summary>Technical details</summary>', '    <ul>'])
        row.extend(f'      <li>{text(point)}</li>' for point in item["details"])
        row.extend(['    </ul>', f'    <p>{text(item["stack"])}</p>', '  </details>'])
    row.append('</article>')
    return "\n".join(row)


def earlier(item):
    source = f'\n  <p>{link(item["link"], item["linkLabel"])}</p>' if item.get("link") else ""
    return f'''<article id="{text(item["id"])}">
  <h3>{text(item["company"])}</h3>
  <p class="entry-meta">{text(item["year"])}</p>
  <p>{text(item["summary"])}</p>{source}
</article>'''


def project(item):
    sample = item.get("sample")
    player = ""
    if sample:
        player = f'''
  <figure>
    <figcaption>{text(sample["label"])}</figcaption>
    <audio controls preload="metadata" aria-label="{text(sample["label"])}" src="{text(sample["file"])}"></audio>
    <details>
      <summary>Transcript</summary>
      <p>{text(sample["transcript"])}</p>
    </details>
  </figure>'''
    return f'''<article id="project-{text(item["id"])}">
  <h3>{text(item["name"])}</h3>
  <p class="entry-meta">{text(item["category"])}</p>
  <p>{text(item["summary"])}</p>
  <p>{link(item["url"], item["linkLabel"])}</p>{player}
</article>'''


def experiment(item):
    name = (link(item["url"], item["name"]) if item.get("url")
            else f'<strong>{text(item["name"])}</strong> ({text(item["category"])})')
    return f'<li id="project-{text(item["id"])}">{name} — {text(item["summary"])}</li>'


def build():
    data = json.loads((ROOT / "data/timeline.json").read_text(encoding="utf-8"))
    sections = {
        "EXPERIENCE": "\n".join(map(experience, data["milestones"])),
        "EARLIER": "\n".join(map(earlier, data["earlier"])),
        "PROJECTS": "\n".join(project(item) for item in data["projects"] if item["featured"]),
        "EXPERIMENTS": "\n".join(experiment(item) for item in data["projects"] if not item["featured"]),
    }
    path = ROOT / "index.html"
    html = path.read_text(encoding="utf-8")
    for section, content in sections.items():
        pattern = rf'^([ \t]*)(<!-- BEGIN {section} -->)\n.*?^\1(<!-- END {section} -->)'
        html, count = re.subn(
            pattern,
            lambda match: f'{match[1]}{match[2]}\n{indent(content, match[1])}\n{match[1]}{match[3]}',
            html,
            flags=re.M | re.S,
        )
        if count != 1:
            raise ValueError(f"Expected one {section} region, found {count}")
    path.write_text(html, encoding="utf-8")
    print("Built index.html from data/timeline.json")


if __name__ == "__main__":
    build()
