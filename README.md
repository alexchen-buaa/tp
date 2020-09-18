# tp: `cd` by Reference

## Introduction

`autojump` really makes my life easier. But when I have to navigate between multiple files / directories with similar names (for example, directories that contains course materials), `autojump` seldom works. And it gets worse because there are new folders with roughly the same names every couple months (notes, textbooks, assignments etc.). 

Another famous solution is `cd` plus `fzf`, which works well in many cases, but it still lacks speed when you're home directory or whatever directory that has a lot of subdirectories in it. This could be dissapointing and prevents this solution from being an overall optimal.

`tp` comes from the idea of combining these tools to get integrated experience in changing directories.

tp is a wrapper for regular `cd **<TAB>` and a `cd` by shortcut script. tp allows users to store `reference: path` pairs, and performs `cd path` when `tp reference` is called. (nothing fancy)

## Commands

+ `tp`: when you call tp without any parameter, it pops out fzf for search.
+ `tp <reference>`: equivalent to `cd path` (given `reference: path` added to config)
+ `tp add <reference> [<path>]`: add reference to config (path is `pwd` if not given)
+ `tp rm <reference>`: remove reference in config

## Installation

You'll need to have `fzf` installed first.

1. find a place to `git clone` this repo
2. put `export TP_INSTALL=<where you put this repo>` in your .zshrc
3. source tp.zsh in your .zshrc
