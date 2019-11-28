# PyGMNormalize
Normalization of gene expression matrices.

## Installation
To install, run the following commands:
```
git clone https://github.com/ficusss/PyGMNormalize.git
cd PyGMNormalize
python setup.py install
```

## Description
This package implements the following metods:
- Total count normalization;
- Percentile normalization;
- Quartile normalization;
- Trimmed mean of M-values normalization.
  ### Input data
  Each of metods takes matrix of gene expression `matrix` as first parameter and some method specific parameters, also some metods take optional parameter `saving_memory` (default `saving_memory=False`) for reduce the RAM usage in the calculations.
  Parameter `matrix` has genes as rows, cells as columns.

## Demonstration
Demonstration of the methods is available [here](https://github.com/ficusss/PyGMNormalize/blob/master/notebooks/demonstration.ipynb).

## Links
- Description of implemented methods is available [here](https://www.hindawi.com/journals/bmri/2015/621690/).
- Description of "Trimmed mean of M-values" method is available [here](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2010-11-3-r25)
