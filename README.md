# Vocalize

Voice control for macOS with a Vim mindset.

## Requirements

- [Miniconda](https://docs.anaconda.com/miniconda/)

## Getting Started

1. Create the virtual environment

   ```sh
   conda activate base
   conda create -n vocalize -y
   conda activate vocalize
   conda config --env --set subdir osx-64
   conda install python=3.10.14 -y
   ```

2. Install Vocalize

   ```sh
   make install
   ```

3. Run Vocalize (use an alias to make this easier)

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
- [Homerow](https://github.com/nchudleigh/homerow)

In addition, the following dotfiles are assumed:

- [dotfiles](https://github.com/joshcummingsdesign/mac-dev-env/blob/master/dotfiles)

See the exact dev environment:

- [mac-dev-env](https://github.com/joshcummingsdesign/mac-dev-env)

Although the project is configured in this specific way, it can be forked and
configured to your liking.

## Acknowledgments

Huge thanks to [David Zurow](https://github.com/daanzu) for all the amazing contributions to the community.

Also thanks to [Tavis Rudd](https://www.reddit.com/r/Python/comments/1atz8d/using_python_to_code_by_voice_tavis_rudd/?rdt=45621) for the inspiration and ideas.
