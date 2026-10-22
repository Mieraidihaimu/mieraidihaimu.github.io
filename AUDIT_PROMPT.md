# Portfolio review brief

Review this static portfolio for accuracy, clarity and usability. Give specific evidence and proportionate severity. A factual contradiction, broken link and stylistic preference should not receive the same priority.

## Sources

- `data/timeline.json`: career and project content.
- `index.html`: introduction, metadata and generated content.
- `scripts/build.py`: generates the marked HTML regions from the JSON.
- `CV_Mier.pdf`: self-reported career history, not independent verification of results.
- `NARRATIVE_PLAN.md`: current editorial decisions.
- `css/styles.css` and `js/app.js`: layout and theme preference.
- [Trepo thesis record](https://trepo.tuni.fi/handle/123456789/21916).
- Public project repositories and live links named in the page. For local-only projects, report the evidence available without assuming a public release exists.

## Accuracy

- Tie Bloomberg’s latency, throughput, uptime and audience numbers to their stated scope. Distinguish service metrics from individual ownership, and CV support from external verification.
- Check Cookpad’s transition from iOS to backend/data engineering in the final year. Do not infer specific streaming response times or consistency guarantees without evidence.
- Keep Farfetch’s China market scope and timeout reduction distinct from company or addressable-market audience figures.
- Include SIQ Basketball, Jerone Group Oy and Nintu Oy with accurate dates.
- Check the thesis description against the archive. Treat its influence on later systems work as a personal reflection, not a claim that the same algorithms provide Kafka ordering guarantees.
- Check every outbound link. Report HTTP reachability separately from a functional project test. Verify any install command before endorsing it.
- Flag unsupported implementation details and measured performance claims. Do not infer speed, correctness or Lighthouse scores from the stack alone.

## Reading experience

Can a visitor quickly find the current role, previous work, three featured projects, CV and contact? Do the optional technical details add substance? Check for repetition, inflated language and unnecessary controls. Recommend further content only when it answers a useful visitor question.

## Implementation

Run `python3 scripts/build.py` and check reproducibility. Content should already be present in HTML, with no content fetch or fallback object. Check local assets and anchors, semantic headings, keyboard focus, native disclosures and both themes. Inspect narrow phone and desktop layouts for overflow and unreadable text. Verify direct file use and disabled JavaScript when the browser supports it; state any verification limits explicitly.

## Report

Lead with material findings, ordered by severity, with the affected file or sentence, supporting evidence and a concrete correction. Separate uncertain claims from confirmed errors and optional editorial suggestions. End with the checks performed and their limits. Avoid inventing issues to fill a quota.
