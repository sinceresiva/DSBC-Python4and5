'''
Implement a Python program to generate all sentences where subject is in ["Americans",
"Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].
'''
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

for subject in subjects:
    for verb in verbs:
        for obj in objects:
            print("{} {} {}".format(subject,verb,obj))
