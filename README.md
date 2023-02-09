# Modular Dictionary Addon

## Development

### Getting Started

```sh
$ python -m venv $VENV_NAME   # I use 'venv'

$ source $VENV_NAME/bin/activate  # Source the script for your shell

$ which pip   # should be /path/to/git_repo/$VENV_NAME/bin/pip

$ pip install --upgrade pip   # Upgrade pip to newest version

$ pip install -r Pipfile.lock   # install dependencies
```

Also make sure to either move your files into the anki2 addon folder or create a link to them using this shell command.
`ln /path/to/git_repo/src/*.py /path/to/anki2/addons21/$ADDON_NAME/`

### Making Changes

Never push directly onto main. Always make changes on a branch and open a pull request so the changes can be reviewed.
