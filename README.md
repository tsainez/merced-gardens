# Merced Botanical Gardens
## Website

## Installation

### Installing Ruby & Jekyll

If this is your first time using Jekyll, please follow the [Jekyll docs](https://jekyllrb.com/docs/installation/) and make sure your local environment (including Ruby) is setup correctly.

### Testing locally

To run the theme locally, navigate to the theme directory and run:

```
bundle install
```

To start the Jekyll local development server.

```
bundle exec jekyll serve
```

To build the theme.

```
bundle exec jekyll build
```

### Github Pages

This theme works with Github Pages. If you are serving from a Project Page or sub-path you must set `baseurl` accordingly in `_config.yml`.
For a custom domain or when serving from the repository root, leave `baseurl` empty (`baseurl: ""`).