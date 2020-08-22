# tp: `cd` by Reference

## Introduction

`autojump` really makes my life easier. But when I have to navigate between multiple files / directories with similar names (for example, directories that contains course materials), `autojump` seldom works. And it gets worse because there are new folders with roughly the same names every couple months (notes, textbooks, assignments etc.). 

Hence, having a filesystem navigator that moves precisely and swiftly (without having to type a lot) would save me a lot of trouble. tp is an attempt to address the issue.

tp allows users to store `reference: path` pairs, and perform `cd path` when `tp reference` is called. (nothing fancy)
