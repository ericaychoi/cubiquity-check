## cubiquity-check
This collection of code is part of Erica and Katerina's project for Georgia Tech's REU (https://jonathansimone.math.gatech.edu/reu2023.html). We aim to distinguish cubiquitous and non-cubiquitous lattices by performing various obstructions.

### checkmod.py
checkmod.py contains all of the functions that can be used to generate specific basis for lattices, compute determinant and the Wu element, generate and check cubes for cubiquity, and more. See comments for more detail.

### results folder
This folder contains both formatted and unformatted data including the list of orthogonal basis for 3D and 4D, results of determinant and wu element obstructions for 3D and 4D, and more. 

### Determinant, Wu element, Projection
Current pipeline for handling determinant and Wu element obstructions is as follows:
* generator.py
    * This generates n-dimensional orthogonal bases
    * n value and matrix dimensions need to be edited before running (can make this more user-friendly in the future)
    * results folder contains outputs in the form of (n)OrthList
* ndDetWuCheck.py
    * Performs Determinant and Wu element obstruction
    * Outputs a nicely formatted file with relevant information
    * results folder contains outputs in the form of (n)DWObs
* failGen.py
    * Performs Determinant and Wu element obstruction
    * Outputs a nested list of bases that are unobstructed by ndDetWuCheck.py that can be manipulated further
    * results folder contains outputs in the form of (n)DWFailList
* projDWFail.py, elsesDWFail.py
    * Given a nested list of matrices, checks whether it is a projection or not
    * projDWFail.py outputs a formatted list of projections
    * elsesDWFail.py outputs a formatted list of non-projections (elses)
        * currently this includes double projections
    * results folder contains outputs in the form of (n)Projs and (n)Elses
