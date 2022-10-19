# Contributing

> **Note**
> This documentation is a WIP and you should always use common sense when reading it. It is intended to be a quick overview of my workflow and not an accurate reference outside (or inside) of this repository. When in doubt or if you have any questions, ask on our Discord server.

## Developer Certificate of Origin

All commits are required to contain a signoff certifying you agree to the [Developer Certificate of Origin](https://developercertificate.org/).

Commits made via the Github web ui should automatically sign off commits. Unfortunately it seems that this doesn't always happen, so if your commit interface doesn't mention "Sign off" anywhere, or look like the image below, add the text `Signed-off-by: Name <email>` to the commit description.

![Github web UI commit button displaying "Sign off and commit changes"](https://user-images.githubusercontent.com/22665282/196296929-bd33aefe-5a3c-4efa-8bae-a7eafe90500e.png#gh-light-mode-only)
![Github web UI commit button displaying "Sign off and commit changes"](https://user-images.githubusercontent.com/22665282/196369582-115dfee5-337c-4061-82ee-be101364daa8.png#gh-dark-mode-only)


If you're not using the Github web UI, you need to either add `-s` or `--signoff` to your git command line options. For instance `git commit --signoff --message "Commit Message"`.

For changes done with VSCode, make sure you select the commit and sign off option instead of the standard commit button.

## Standards

To the extent possible, anything you write or edit should follow the commonmark standard with the addition of the extra extensions included (which you can currently find listed in the [mkdocs.yml](mkdocs.yml)

Anything outside of the `docs/` directory is not included in the final build. That mean any images included within your markdown should be well organized in their own folder near your files.

Documentation for mkdocs-material can be found at [https://squidfunk.github.io/mkdocs-material/getting-started/](https://squidfunk.github.io/mkdocs-material/reference/)


## GithHub web ediitor

Simple fixes can easily be done online through the GitHub editor, and proposed via pull request. All pages use markdown for styling with some extra extensions which won't be shown in GitHubs preview. Edits can also be suggested via creating an issue on GitHub.

## Gitpod

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/unturned-info/unturned-3-knowledgebase)

Gitpod is an online service that provides an automatically provisioned VSCode instance. If you want a better editing experience than using the Github online editor, but don't want to deal with installing VSCode and all of our dependencies to review your changes, it may be worth a try.

## Github.dev

If you want VSCode for simpler changes, you can open github.dev by pressing `.` (that's a period) almost anywhere on github to get a quick cut down VSCode instance.

## Locally

> **Note**
> This section is intended for more advanced users with some knowledge of text editors and version control

If you plan to work with the repository on your own computer, you'll want to first fork it on github via the fork button on the upper right, then clone your fork using git. Make sure you remember to sign off your commits as mentioned above, or else you'll have to go back and fix them with more advanced git features.

In order to preview or test the site, you'll need to have a recent version of python installed (>=3.7) as well as the sites dependencies. To install it's python dependencies, run `pip install -r requirements.txt` in a terminal or install PDM and run `pdm sync`.

The MKdocs dev server is ran with `mkdocs serve` or `pdm serve`, depending on whether you installed the dependencies with pip or pdm. It can be exited with ctrl+c.
