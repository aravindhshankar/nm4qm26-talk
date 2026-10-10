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
                        \sitemap, \legend, \nf/\of (page-trim figure includes, being phased out)
talk/sections/NN_*.tex  one file per section, a few frames each
talk/figures/           the user's original figure PDFs
talk/nm4qm_talk.pdf     tracked: a working presentation is always in the repo
talk/build.sh           the USER's build script: builds and opens the PDF (-w = live preview)
```
Subagent build: `cd talk && latexmk -pdf -interaction=nonstopmode nm4qm_talk.tex`, then
`latexmk -c` and remove `*.nav *.snm`. Do not run `build.sh` from a subagent (it opens a window).

## Who does what (token efficiency)
- Opus (the main session) talks with the user and thinks: structure, physics, wording, critique.
- Opus does not edit .tex, compile, or check formatting itself. That goes to a subagent:
  - haiku: mechanical work (text edits to an agreed spec, compile and check, renames, swapping a figure file).
  - sonnet: anything with design in it (a new frame, TikZ, layout problems, figure crops).
  - Pick by a quick guess. Do not spend tokens deciding which model to use.
- The subagent compiles, renders the changed frame(s) to PNG, checks them, and reports.
  Opus then looks only at the final rendered frame(s), not at intermediate output.
- Give the subagent the exact section file to edit and the agreed spec; it should not read
  the whole deck or the papers.
- In our chats the subagent does all builds. `build.sh` is only for when the user works alone.

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
- Figures carry the slide: assertion-style title (the claim, not the topic), one dominant
  figure, at most 3 short bullets or one key equation, optional one-line take-away.
- Regime colours are fixed across the deck (see `macros.tex`): free moment red, Kondo blue,
  AFM singlet green, FM two-stage orange.
- Keep the .tex hand-editable: the user edits offline too. Plain beamer, one section per file,
  no generated code, no clever macros. Prefer editing one section file per change.
- Speaker notes are `% Notes:` comments under each frame.

## Known limitation
Until every `\nf`/`\of` include is replaced by a file in `talk/figures/`, a fresh clone needs the
two paper PDFs in the repo root to compile. The tracked `talk/nm4qm_talk.pdf` is always usable.
