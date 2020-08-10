# Contributing

Note:
This documentation is a WIP and you should always use common sense when reading it. It is intended to be a quick overview of my workflow and not an accurate reference outside (or inside) of this repository

## Online

Simple fixes can easily be done online through the GitHub editor, and proposed via pull request. All pages use markdown for styling with some extra extensions which won't be shown in GitHubs preview. Edits can also be suggested via creating an issue on github.

## Locally

More advanced changes are best done locally via forking and cloning the repo locally. After you've completed your changes you can submit a pull request to the main repository from your fork, and it will be reviewed.

### Advanced local editing

If you are planning on writing  or editing a larger amount of markdown, its worth getting an environment that suites you. I personally use VSCode with Spell Right, Markdown All in One, and markdownlint along with some git related extensions. Visual studio lets you easily preview some markdown (but not the extensions the full site uses)

For previewing within the site, you can install mkdocs-material via pip `pip install mkdocs-material` and run it's local development server `mkdocs serve` in the repository directory.

Documentation for mkdocs-material can be found at <https://squidfunk.github.io/mkdocs-material/getting-started/>

## GitHub pages deployment

MKdocs is deployed to GitHub pages via an action that runs on all commits to master. It generates documentation and pushes it to the gh-pages branch, which GitHub uses to serve the site.
