set nocompatible            " disable compatibility to old-time vi
set showmatch               " show matching 
set ignorecase              " case insensitive 
set mouse=v                 " middle-click paste with 
set hlsearch                " highlight search 
set incsearch               " incremental search
set tabstop=2               " number of columns occupied by a tab 
set softtabstop=2           " see multiple spaces as tabstops so <BS> does the right thing
set expandtab               " converts tabs to white space
set shiftwidth=2            " width for autoindents
set autoindent              " indent a new line the same amount as the line just typed
set number                  " add line numbers
set wildmode=longest,list   " get bash-like tab completions
set cc=200                  " set an 80 column border for good coding style
filetype plugin indent on   " allow auto-indenting depending on file type
"syntax on                  " syntax highlighting
set mouse=a                 " enable mouse click
set clipboard=unnamedplus   " using system clipboard
set cursorline              " highlight current cursorline
set ttyfast                 " Speed up scrolling in Vim
set spell                   " enable spell check (may need to download language package)
"set noswapfile             " disable creating swap file
"set backupdir=~/.cache/vim " Directory to store backup files.

" TODO
" - Need a theme
" - Review Docs and configure plugins
" - Split up configs, individually and by vim/nvim
" - Fallback vim plugins for the nvim exclusives

" Plug Plugin Manager
call plug#begin()

" Install Help Pages
Plug 'junegunn/vim-plug'
" Indentation hints
Plug 'lukas-reineke/indent-blankline.nvim'
" Gutter Markings for Git
Plug 'lewis6991/gitsigns.nvim'
" Git Integration
Plug 'tpope/vim-fugitive'
" Not sure
Plug 'nvim-treesitter/nvim-treesitter', { 'branch': 'main' }
" Linter
Plug 'mfussenegger/nvim-lint'
" Auto pair brackets, maybe more?
Plug 'windwp/nvim-autopairs'
" Lots of debugging and view stuff
Plug 'folke/trouble.nvim'
" Breakpoints and Debugging Integration
Plug 'mfussenegger/nvim-dap'
" Latex Support
Plug 'lervag/vimtex'
" File Explorer
Plug 'nvim-neo-tree/neo-tree.nvim'
  " Backend Utilities, Required
  Plug 'nvim-lua/plenary.nvim'
  " UI Library, Required
  Plug 'MunifTanjim/nui.nvim'
  " Nerd Font Icons, Optional
  Plug 'nvim-tree/nvim-web-devicons'
  " LSP Operations
  Plug 'antosha417/nvim-lsp-file-operations'
  " Pretty UI Library, Optional
  Plug 'folke/snacks.nvim'
    " Mini UI Icons, Optional
    Plug 'nvim-mini/mini.icons'
  " Image Support, Optional
  Plug '3rd/image.nvim'
  " Window Picker Prompt, Optional
  Plug 's1n7ax/nvim-window-picker'

call plug#end()

