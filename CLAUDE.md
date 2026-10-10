# NM4QM 2026 talk — working rules for Claude

Claude maintains this file. Update it whenever the user changes how we work.
If anything here is unclear or conflicts with what the user says, ask the user.

## What this is
15-minute conference talk, "Kondo and RKKY interactions in bilayer graphene"
(A. S. Shankar, ICTP), LaTeX beamer. We are reworking it section by section, slide by slide.

## Start of a session
1. Read `notes/paper_notes.md` (paper facts, figure index, talk decisions, Q&A prep, open items).
2. Do NOT re-read `rkky_kondo.pdf` / `KondoTBG.pdf` unless a needed fact is missing from the
   notes. If you do look something up, add it to the notes.
3. `git log --oneline -10` and `git status` to see where we are. The user also edits by hand
   (offline), so uncommitted changes may be theirs: ask before overwriting or committing them.

## Layout
```
CLAUDE.md, .gitignore, .claude/settings.json
notes/paper_notes.md
talk/nm4qm_talk.tex     main file: only \input lines
talk/preamble.tex       theme, packages, colours, footline
talk/macros.tex         title/author, \ft (frame title), \tk (take-away box), regime colours,
                        \sitemap, \legend
talk/sections/NN_*.tex  one file per section, a few frames each
talk/figures/           all figures, included with plain \includegraphics{figures/...}:
                        the user's original draft-figure PDFs (do not rename or edit) and
                        tbg_*.png crops from the published TBG paper. Map: notes/paper_notes.md
talk/nm4qm_talk.pdf     tracked: a working presentation is always in the repo
talk/build.sh           the USER's build script: builds and opens the PDF (-w = live preview)
talk/preview.tex        section preview: same preamble, one \input line. Builds preview.pdf
                        (gitignored) so a single section can be iterated on alone.
```
Subagent build while iterating on a section: put that section in `talk/preview.tex`, then
`cd talk && latexmk -g -pdf -interaction=nonstopmode preview.tex` (short log, pages start at 1).
Before a commit: one full build, `latexmk -g -pdf -interaction=nonstopmode nm4qm_talk.tex`,
so the tracked PDF is always the whole talk. After either: `latexmk -c`, remove `*.nav *.snm`.
macOS has no `timeout` command. Do not run `build.sh` from a subagent (it opens a window).

## Who does what (token efficiency)
- Opus (the main session) talks with the user and thinks: structure, physics, wording, critique.
- Building from scratch goes to a subagent:
  - sonnet: a new frame, a new TikZ drawing, figure crops, a first layout.
  - haiku: mechanical bulk work (renames, swapping a figure file, the same edit in many places).
  - Pick by a quick guess. Do not spend tokens deciding which model to use.
- Fine-tuning an existing frame is done by Opus directly (user, 2026-10-10): spacing, sizes,
  column widths, line breaks, wording, small TikZ nudges. Edit the section file, build with
  `preview.tex`, render and look at just the changed page. A subagent polish round cost
  90–175k tokens for a few lines of change, so it is not worth delegating.
- Never have Opus and a subagent edit the same file at the same time.
- The subagent compiles, renders the changed frame(s) to PNG, checks them, and reports.
  Opus then looks only at the final rendered frame(s), not at intermediate output.
- Give the subagent the exact section file to edit and the agreed spec; it should not read
  the whole deck or the papers.
- In our chats Claude (subagent or Opus) does all builds, with latexmk. `build.sh` is only for
  when the user works alone; Claude never runs it (it opens a window).

## Work loop for each slide
1. Discuss with the user.
2. Opus writes a short spec in chat: frame title, figure, bullets, take-away line.
3. The user OKs it (or edits it). Do not build before the OK.
4. Subagent builds. Opus checks the rendered frame and tells the user it is ready to look at.
5. When the user accepts and it compiles: commit.

## Git
- Single checkout on `main`; the worktree guard is off for this repo (`.claude/settings.json`),
  at the user's request. Do not run several Claude jobs on this repo at once.
- Auto-commit each accepted change that compiles. One short message line. Include the rebuilt PDF.
- Never push; the user pushes.
- Never commit `rkky_kondo.pdf` (unpublished draft) or `KondoTBG.pdf`. Both are gitignored.
  Never commit a cropped PDF made from the draft: it still holds the hidden page text.
  If a figure must be extracted from the draft, use a 400-dpi PNG.
- Never touch `sample_talk/` (unrelated talk, kept only for its colour scheme).

## Slides
- Professional. "Goldilocks" text: only as much as needed to communicate, no more, not too little.
- Figures carry the slide: one dominant figure, at most 3 short bullets or one key equation,
  optional one-line take-away.
- Titles are SHORT (user, 2026-10-10: "the titles in general are too verbose"). Aim for one
  phrase of about 4 to 7 words, e.g. "van Hove singularities in the flat band",
  "Kondo revival at the magic angle". Not a full sentence with a colon and two clauses.
  The same goes for the grey take-away line: short, and a question is fine.
- Text colours must not clash with the curve colours of the figure they annotate; do not draw
  label arrows across data. Prefer a caption beside or under the figure.
- Cite the source of every borrowed figure under it.
- Highlights: the user's inline colour blocks, as in `sample_talk/talk_NQS_basis_dependence.tex`:
  `\colorbox{tomato!30}{\mystrut key phrase}` then normal text. Colours tomato, spinach, pumpkin,
  orchid, citron (all in `preamble.tex`, with `\mystrut`), tint `!30` to `!60`. Use them for a
  short label or key phrase, a few per slide at most, not for whole paragraphs.
  Caution (Claude's note): spinach is the same RGB as the AFM regime green and pumpkin is close
  to the FM orange, so on slides that show those regimes pick a different highlight colour.
- A dense slide is fine if every ingredient on it is simple and is explained clearly
  (conference talks move fast). Use beamer overlays (`\only`, `\onslide`) to bring a dense
  slide in step by step; keep the layout from jumping between steps.
- References: small grey full reference directly under the figure or claim it belongs to,
  typed as plain text. Use them throughout, but sparingly: at most two or three per slide.
- Regime colours are fixed across the deck (see `macros.tex`): free moment red, Kondo blue,
  AFM singlet green, FM two-stage orange.
- Keep the .tex hand-editable: the user edits offline too. Plain beamer, one section per file,
  no generated code, no clever macros. Prefer editing one section file per change.
- Speaker notes are `% Notes:` comments under each frame.

## Figures
The deck compiles from the repo alone; no .tex file references the paper PDFs. Keep it that way.
A new figure from the draft: ask the user for the original PDF. From the published TBG paper:
400-dpi PNG crop into `talk/figures/tbg_*.png`. From the user's old talk
(`assets/prev_tbg_talk.pdf`): 400-dpi PNG crop into `talk/figures/prev_*.png`.
