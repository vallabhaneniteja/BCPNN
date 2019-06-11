# BCPNN
Implementation of BCPNN(Bayesian Confidence Propagation Neural Network) method used to predict ADR(Adverse Drug Reaction) Signals

Database:
The database used is that of the FDA ADR reports.

bcpnn.py:
Calls the remaining codes and outputs the drug-adr pairs along with their signals.
If the required drug-adr pair is not present it means that their is no or negative relation between the drug and adr.

bcpnn_parameters.py:
Contains the functions required to calculate the expectation, information component, variance and also whether for given values
the signal is strong, medium, or weak.

bcpnn_data.py:
Does the data cleaning part of the fda database using csv readers and stores them in a dictionary.

Method of Execution:
The required files from FDA are the drug and the react files(The most recent at the time of writing are DRUG19Q1.txt and REACT19Q1.txt files) and keep them in the same directory as the python codes and run the bcpnn.py(Required packages are csv, collections, math most of which come with python).

Output:
Alpha.csv which contains the drug along with parameters are updated. The same is done with beta.csv which contains the adr's along with their parameters and gamma.csv which contains the drug-adr pairs along with their paramaters.
The drug-adr pair along with the signals is stored into a dictionary and input is taken for what drug adr pair the signal is required.
