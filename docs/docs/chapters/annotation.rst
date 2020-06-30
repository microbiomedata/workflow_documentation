The Annotation Workflow
==================

IMG annotation workflow

Summary
-------

Workflow Diagram
------------------

TODO: Image
TODO: Need a Cromwell generated diagram from WDL definition of the workflow

Workflow Dependencies
---------------------

Third party software
~~~~~~~~~~~~~~~~~~~~

- Conda (3-clause BSD)
- tRNAscan-SE >= 2.0 (GNU GPL v3)
- Infernal 1.1.2 (BSD)
- CRT-CLI 1.8 (Public domain software, last official version is 1.2, I made changes to it based on Natalia's and David's suggestions)
- Prodigal 2.6.3 (GNU GPL v3)
- GeneMarkS-2 >= 1.07 (Academic license for GeneMark family software)
- Last >= 983 (GNU GPL v3)
- HMMER 3.1b2 (3-clause BSD, I am using Bill's thread optimized hmmsearch)
- SignalP 4.1 (Academic)
- TMHMM 2.0 (Academic)

Database 
~~~~~~~~~~~~~~~~
- Rfam (Creative Commons Zero ("CC0"))
- KEGG (Paid Subscription, getting KOs/ECs indirectly via IMG NR)
- SMART (Academic)
- COG (Free, couldn't find one, HMMs created from the 2003 models)
- TIGRFAM (Free, couldn't find one)
- SUPERFAMILY (Academic)
- Pfam (GNU Lesser General Public License, according to its wikipedia page)
- Cath-FunFam (Free, couldn't find one)

Workflow Availability
---------------------
Git repo:

TODO: separate repo

https://github.com/microbiomedata/WorkflowPlanning/tree/master/AssemblyPipeline

Container:


Test datasets
-------------


Details
---------------------

Inputs
~~~~~~~~

Outputs
~~~~~~~~

Requirements for Installation
----------------------------

- Linux (with sh/bash)
- Python >= 3.6 (via conda)
- Java >= 1.8 (via conda)
