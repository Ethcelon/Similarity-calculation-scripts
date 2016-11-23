# Similarity-calculation-scripts
Some scripts to calculate similarity metrics of files that I wrote for malware analysis coursework.

These scripts have 2 purposes:
* Automate other scripts.
* Perform calculations and output CSV files.

They automate the following:

https://github.com/hdg7/EnTS

https://github.com/hdg7/NCD

To use ents_1, ents_2, first clean the folder ( I start with a new folder for each set of EnTS calculations):

!!! Do not run if you don't understand what is going on !!!
```
rm -r test/;
rm -r recon/;
rm or*;
rm sub*;
rm seg*;
rm wav*;
rm rec*;
rm file*;
```

Run this. It's the same as ents_1.py , but ents_1.py does not work. I have to figure out some silly thing I missed.

```
mkdir test recon;
for f in ../folder/*.format;
do
    ./entCalculator -i $f;
done;
mv segm* test/;
mv rec* recon/;
rm -r sub*;
rm -r or*;
rm -r wav*;
```
To do the calculations:

```python ents_2.py```

Using automate1.py

I'm calculating NCD and CR here, just edit the python file to something that suits your need (mostly just automation)

