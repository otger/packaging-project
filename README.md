# Example Package

This is a simple example package meant as an example on how to setup a python package with a console script

# test pypi
## Build and upload to testpypi:

```
cd packaging-project
python -m build
python3 -m twine upload --repository testpypi dist/*
```

## Install from testpypi

```
pip install --index-url https://test.pypi.org/simple/ --no-deps my-echo-otger
```

# PyPi

## Build and upload to testpypi:

```
cd packaging-project
python -m build
python3 -m twine upload dist/*
```


----
You can use [Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/) to write your content.

