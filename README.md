# pcc - **pycache** Cleaner

A simple utility to recursively find and remove all `__pycache__` folders.

## Installation

This project uses `uv`. If you don't have `uv` installed, you can find the installation instructions [here](https://github.com/astral-sh/uv#installation).

Install UV with:

```
pipx install uv .
```

Once `uv` is installed, you can install the dependencies and the tool by running:

```bash
cd path/to/pycachecleaner
uv sync
uv tool install .
```

Alternatively, you can use `pip`:

```bash
pip install .
```

This will register the tool as `pcc`

## Usage

To remove all `__pycache__` folders in the _**current directory**_ and its subdirectories, simply run:

```bash
pcc
```

You can also specify a different root directory:

```bash
pcc /path/to/your/project
```

The tool will print the number of `__pycache__` folders that were removed.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
