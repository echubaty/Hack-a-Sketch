# Compiles pygame on homebrew for distribution.
# This may not be what you want to do if not on travisci.

brew update
brew unlink pkg-config
brew install pkg-config
brew link pkg-config
brew unlink libpng
brew unlink libtiff

# brew install ccache
# export PATH=/usr/local/opt/ccache/libexec:$PATH

brew uninstall --force sdl
brew uninstall --force sdl_image
brew uninstall --force sdl_mixer
brew uninstall --force sdl_ttf
brew uninstall --force smpeg
brew uninstall --force jpeg
brew uninstall --force libpng
brew uninstall --force libtiff
brew uninstall --force webp
brew uninstall --force flac
brew uninstall --force fluid-synth
brew uninstall --force smpeg
brew uninstall --force libmikmod
brew uninstall --force libvorbis
brew uninstall --force portmidi
brew uninstall --force freetype
brew install sdl --without-x --universal
brew install jpeg --universal
brew install libpng --universal
brew install libtiff --universal --with-xz
brew install webp --universal --with-libtiff --with-giflib
brew install libvorbis --universal
brew install libogg --universal
brew install flac --universal --with-libogg
brew install fluid-synth
brew install libmikmod --universal
brew install smpeg
brew install portmidi --universal
brew install freetype --universal
brew install sdl_ttf --universal

brew install sdl_image --universal
brew install sdl_mixer --with-flac --with-fluid-synth --with-libmikmod --with-libvorbis --with-smpeg
