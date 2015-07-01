set nocompatible
filetype off

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()
Plugin 'gmarik/Vundle.vim'
Bundle 'Rykka/riv.vim'
call vundle#end()

filetype plugin indent on


" solarized vim :3
set background=dark
colorscheme solarized

set tabstop=4
set shiftwidth=4
set expandtab

syntax enable
set smartcase
set incsearch
set showmatch
set hlsearch
set number
