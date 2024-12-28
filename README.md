# Modeling Swiss farmer's attitudes about climate change

## Modeling data from [Kreft et al. 2020](https://www.sciencedirect.com/science/article/pii/S2352340920303048).

## In this tutorial, we'll compare ML models across two different Git branches of a project- and we'll do it in a continuous integration system (GitHub Actions) for automation superpowers! We'll cover:

## Why comparing model metrics takes more than a git diff

## How pipelines, a method for making model training more reproducible, help you standardize model comparisons across Git branches

## How to display a table comparing model performance to the main branch in a GitHub Pull Request



## build dvc pipeline to run get_data.py -> process_data.py -> train.py
## to create dvc.yaml run -


dvc run -n get_data -d get_data.py -o raw_data.csv --no-exec python get_data.py


## update dvc.yaml for process_data.py and train.py
## save dvc.yaml and run dvc repro in terminal to run the pieline


## Add repo to Git

git add -A
git commit -m "add repo to dheeraj"

git remote add origin https://github.com/dspkgp/farmer.git

git push -u origin main

## create new branch

git checkout -b experiment
git pull origin main
git push origin experiment


