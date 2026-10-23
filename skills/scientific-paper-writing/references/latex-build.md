# Bounded LaTeX Build Guide

Build the existing manuscript in the environment where delivery is intended.
Inspect its main file, document class, bibliography setup and existing build command
before choosing tools. Do not assume the host, TeX distribution or engine from a
previous session. A build request does not authorize installing TeX or running
untrusted document code with unrestricted shell access.

## Select an available, compatible engine

On a POSIX host, inspect only the relevant existing commands, for example:

```bash
command -v latexmk
command -v pdflatex
command -v xelatex
command -v lualatex
command -v bibtex
command -v biber
```

On other hosts use native command discovery, not these commands through an invented
bridge. Prefer the project's existing build recipe. `latexmk` is a driver, not
proof that its selected TeX engine or bibliography tool is installed. Choose the
engine required by the document's packages/fonts and journal template. Do not
silently change the class, bibliography backend or scientific content to hide a
missing dependency.

## Compile without destroying work

- Identify the main `.tex` file and use relative paths for included files, figures
  and bibliography. Do not embed developer home or host-specific paths in the paper.
- Use non-interactive execution, a bounded timeout and a retained build log. For
  compatible TeX engines, `-interaction=nonstopmode -halt-on-error -file-line-error`
  helps expose the first actual error. Pass flags through the real project's
  driver correctly; do not invent a universal build command.
- Disable unrestricted shell escape. Do not execute downloaded macros, scripts or
  project configuration blindly; a trusted exception needs explicit authorization.
- Preserve source, figures and bibliographies. Use the established output directory
  or a new owned build directory; do not clean broad paths or delete unrecognized
  work. Distinguish a freshly produced PDF from an old file left by a failed build.
- Run the required bibliography and cross-reference passes through the existing
  toolchain. A PDF with unresolved citations, missing figures or broken references
  is not a finished submission artifact merely because a TeX pass exited zero.

## Diagnose and report the actual failure

Read the first consequential error and its source context: a missing engine,
package/font, bibliography tool, input file, invalid macro and permission failure
need different interventions. Do not repeat the same failing command without a
changed hypothesis or repair. Installing or upgrading the toolchain is an operator
decision; a missing local engine does not mean the manuscript cannot be compiled
on an approved equipped host.

Report the command/environment actually used, its exit status, new PDF if produced,
and consequential log warnings/errors. Inspect layout and figures when that review
is authorized; syntax/build success is not visual acceptance or scientific validity.
