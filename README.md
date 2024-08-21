# Vocalize

Voice control for macOS with a Vim mindset.

## Requirements

- [miniconda](https://docs.anaconda.com/miniconda/)

## Getting Started

1. Create the virtual environment

   ```sh
   conda create -n vocalize -y
   conda activate vocalize
   conda config --env --set subdir osx-64
   conda install python=3.10.14 -y
   ```

2. Install Vocalize

   ```sh
   make install
   ```

3. Run vocalize (use an alias to make this easier)

   ```sh
   make start
   ```

## Keybindings

This project assumes you have the following keybindings configured:

- Dictation: Control + Shift + D
- Password Manager: Command + Option + \
- Terminal Show/Hide: Command + Shift + Space
- Clipboard Manager: Control + Space

And the following apps installed:

- [Rectangle](https://github.com/rxhanson/Rectangle)

In addition, the following dotfiles are assumed:

- [dotfiles](https://github.com/joshcummingsdesign/mac-dev-env/blob/master/dotfiles)

See the exact dev environment:

- [mac-dev-env](https://github.com/joshcummingsdesign/mac-dev-env)

Although the project is configured in this specific way, it can be forked and
configured to your liking.
