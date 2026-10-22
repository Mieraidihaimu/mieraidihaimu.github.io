# Portfolio editorial plan

The site should make it easy to understand Mier’s work, inspect a few details and get in touch. The main thread is the move from native iOS apps to backend messaging infrastructure, with independent software showing ongoing curiosity.

## Reading order

1. A short introduction with role, focus, CV and profile links.
2. Four concise career entries, with optional technical details for the recent roles.
3. Earlier work and education in a disclosure. Include SIQ Basketball, Jerone Group Oy and Nintu Oy with the dates from the CV. Keep the computer vision thesis connection as a personal influence, rather than equating vision algorithms with Kafka ordering guarantees.
4. Three selected projects: Pagehum, TypingPall and Türkic Grid Games. Keep the other five as short entries under “A few more experiments”.
5. An email contact.

## Evidence and wording

- Bloomberg’s 40% latency reduction, 25% throughput improvement, 99.99% service uptime and 200,000+ mobile DAU come from the supplied CV. These are self-reported professional results, not independently audited benchmarks. Keep service scale in the relevant role’s technical details.
- Remove Farfetch’s 150M user claim. Retain the China market scope and the CV’s 65% reduction in API/CDN timeouts; do not substitute an unrelated company audience figure.
- Describe Cookpad SSE as progressive response rendering. No zero-latency or precise time-to-first-content claim without measurement evidence.
- TypingPall’s public source repository and build instructions are available. Omit the Homebrew command until the tap can be verified publicly.
- Do not promise a Lighthouse score, bundle size, memory footprint or project latency without a reproducible measurement. Use system fonts to avoid external font requests.
- Describe the monitor as C99/POSIX with SQLite, rather than “zero dependencies”. Do not link local projects to an unrelated or unavailable repository.
- Prefer “built”, “led”, “reduced” and specific scope over slogans, superlatives or inferred implementation details.

## Implementation

`data/timeline.json` is the content source for experience, earlier work and projects. Run `python3 scripts/build.py` after editing it. The script updates the marked regions in `index.html`; edit the introduction, navigation and contact directly in that file.

The output is static HTML and CSS with a small theme preference script. Native `details` disclosures work with JavaScript disabled and over `file://`. There are no content fetches, external fonts or runtime packages.
