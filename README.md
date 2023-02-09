# Modular Dictionary Addon

## Installation

### Manual Installation

<Details>
<Summary>Windows</Summary>

```sh
# Clone the addon contents
$ git clone https://github.com/OrangeRed/anki-mod-dictionaries.git

# Copy the addon contents into the Anki Addon folder
$ cp -r anki-mod-dictionaries/src %AppData%/anki2/addons21/
```

After copying the code from the git repository into the anki addon folder the addon will be active when you start anki.

Also it is recommended that you rename the folder to something else since having an addon called `src/` is a bit unsanitary.

</Details>

<br/>

<Details>
<Summary>MacOS</Summary>

```sh
# Clone the addon contents
$ git clone https://github.com/OrangeRed/anki-mod-dictionaries.git

# Copy the addon contents into the Anki Addon folder
$ cp -r anki-mod-dictionaries/src ~/Library/Application Support/Anki2/addons21/
```

After copying the code from the git repository into the anki addon folder the addon will be active when you start anki.

Also it is recommended that you rename the folder to something else since having an addon called `src/` is a bit unsanitary.

</Details>

<br/>

<Details>
<Summary>Linux</Summary>

```sh
# Clone the addon contents
$ git clone https://github.com/OrangeRed/anki-mod-dictionaries.git

# Copy the addon contents into the Anki Addon folder
$ cp -r anki-mod-dictionaries/src ~/.local/share/anki2/addons/
```

After copying the code from the git repository into the anki addon folder the addon will be active when you start anki.

Also it is recommended that you rename the folder to something else since having an addon called `src/` is a bit unsanitary.

</Details>

<hr/>

## Frequently Asked Questions

**Q. Will you support Japanese pitch accent generation?**

**A.** Not directly, but it is always possible to import a dictionary with that information and use that for generation. For people looking to generate readings and pitch accent information inline consider using the [Japanese Reading and Pitch Accent](https://github.com/Ben-Kerman/anki-jrp) addon.

**Q. Will you support word audio look up from sources like Forvo?**

**A.** Not directly, but it is always possible to import a dictionary with audio files and use that for looking up words.
For people looking to get audio of Japanese words consider using [Yomichan](https://foosoft.net/projects/yomichan/) as the extension provides audio for most Japanese words.

## Development

### Getting Started

```bash
# Set up the python virtual environment. Convention is to call it 'venv'
$ python -m venv $VENV_NAME

# Source the correct script for your shell
$ source $VENV_NAME/bin/activate

# Verify that venv is active.
# The path should be /path/to/git_repo/$VENV_NAME/bin/pip
$ which pip

# Upgrade pip to latest version
$ pip install --upgrade pip

# Install project dependencies and linter / auto formatter
$ pip install -r pyproject.lock
```

Also make sure to either move your files into the anki2 addon folder or create a link to them using this shell command.
`ln /path/to/git_repo/src/*.py /path/to/anki2/addons21/$ADDON_NAME/`

### Making Changes

Never push directly onto main. Always make changes on a branch and open a pull request so the changes can be reviewed.
