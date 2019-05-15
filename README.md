# *< Project Title >*

*A short description of the project*

## Table of Contents

* [1. Conceptual Architecture](1-Technical-Architecture)
* [2. Technical Architecture](1-Technical-Architecture)
* [3. Technologies](3-Technologies)
* [4. Manual](4-Manual)
* [5. Github-WorkFlow]()

## 1. Conceptual Architecture
*In this section explain the train/predict conceptual architecture that the aplication has.*
*We can add the train/predict conceptual architecture diagram.*

## 2. Technical Architecture
*In this section explain the deployed train/predict architecture that the aplication has.*
*We can add the train/predict architecture diagram.*

## 3. Technologies

*List of the Technologies that the project use*

*Example:*

|AWS|Languages|CI/CD|
|---|---------|-----|
|S3|Python < Version >|Docker|

## 4. Manual

*In this section, please put the detail (step by step) for make an execution, the code lines that an user has to make to make a complete execution of the algorithm*

```Python
print('Code goes here!')
```

## 5. GitHub WorkFlow

We use a modified version of Gitflow:

### 5.1 Versioning

- `v-{major}-{minor}`
  - `major` for new features
  - `minor` for hotfixes

### 5.2 Features

1. Create new branch `feature/{short-description}` using `development` as base
2. Work on it normally
3. Open pull request to `development` when done
4. Merge it to `development`
5. Open pull request from `development` to `master` when doing a new release
6. Merge it to `master`
7. Tag it as appropriate using the versioning scheme (increase the major version by one
and reset the minor version to zero)

### 5.3 Hotfixes

1. Create new branch `hotfix/{short-description}` using `master` as base
2. Work on it normally - hotfixes should be extremely small
3. Open pull request when is done
4. Merge it to `master`
5. Tag it as appropriate using the versioning scheme (keep same major, increase
minor version by one)

## 6. Code Guidelines

Most of the code is written in Python and tries to follow the [PEP8 standard](https://www.python.org/dev/peps/pep-0008/).

Documentation follows the [Google documentation guidelines](http://google.github.io/styleguide/pyguide.html?showone=Comments#Comments). [Example](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
