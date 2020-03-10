
< Project Title >
=================================

[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20OS%20X%20%7C%20Windows%20-blue.svg)](https://github.com/JohnnyLVP/Project-Standar-Documentation/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/JohnnyLVP/Project-Standar-Documentation.svg)](https://github.com/JohnnyLVP/Project-Standar-Documentation/network)
[![GitHub stars](https://img.shields.io/github/stars/JohnnyLVP/Project-Standar-Documentation.svg)](https://github.com/JohnnyLVP/Project-Standar-Documentation/stargazers)



*A short description of the project*

## Table of Contents

* [1 Github WorkFlow](#1-github-workflow)
* [2 Code Guidelines](#2-code-guidelines)
* [3 Conceptual Architecture](#3-conceptual-architecture)
* [4 Technical Architecture](#4-technical-architecture)
* [5 Technologies](#5-technologies)
* [6 Manual](#6-manual)


## 1. GitHub WorkFlow

We use a modified version of Gitflow:

### 1.1 Versioning

- `v-{major}-{minor}`
  - `major` for new features
  - `minor` for hotfixes

### 1.2 Features

1. Create new branch `feature/{short-description}` using `develop` as base
2. Work on it normally
3. Open pull request to `develop` when done
4. Merge it to `develop`
5. Open pull request from `develop` to `master` when doing a new release
6. Merge it to `master`
7. Tag it as appropriate using the versioning scheme (increase the major version by one
and reset the minor version to zero)

### 1.3 Hotfixes

1. Create new branch `hotfix/{short-description}` using `master` as base
2. Work on it normally - hotfixes should be extremely small
3. Open pull request when is done
4. Merge it to `master`
5. Tag it as appropriate using the versioning scheme (keep same major, increase
minor version by one)

## 2. Code Guidelines

Most of the code must be written in Python and tries to follow the [PEP8 standard](https://www.python.org/dev/peps/pep-0008/).

Documentation follows the [Google documentation guidelines](http://google.github.io/styleguide/pyguide.html?showone=Comments#Comments). [Example](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).



## 3. Conceptual Architecture
*In this section explain the train/predict conceptual architecture that the aplication has.*
*We can add the train/predict conceptual architecture diagram.*

## 4. Technical Architecture
*In this section explain the deployed train/predict architecture that the aplication has.*
*We can add the train/predict architecture diagram.*

## 5. Technologies

*List of the Technologies that the project use*

*Example:*

|AWS|Languages|CI/CD|
|---|---------|-----|
|S3|Python < Version >|Docker|

## 6. Manual

*In this section, please put the detail (step by step) for make an execution, the code lines that an user has to make to make a complete execution of the algorithm*

```Python
print('Code goes here!')
```
