# tp: `cd` by Reference

## Introduction

`autojump` really makes my life easier. But when I have to navigate between multiple files / directories with similar names (for example, directories that contains course materials), `autojump` seldom works. And it gets worse because there are new folders with roughly the same names every couple months (notes, textbooks, assignments etc.). 

Hence, having a filesystem navigator that moves precisely and swiftly (without having to type a lot) would save me a lot of trouble. tp is an attempt to address the issue.

tp allows users to store `reference: path` pairs, and performs `cd path` when `tp reference` is called. (nothing fancy)

## Commands

+ `tp <reference>`: equivalent to `cd path` (given `reference: path` added to config)
+ `tp add <reference> [<path>]`: add reference to config (path is `pwd` if not given)
+ `tp rm <reference>`: remove reference in config

## Installation

1. find a place to `git clone` this repo
2. put `export TP_INSTALL=<where you put this repo>` in your .zshrc
3. source tp.zsh in your .zshrc
