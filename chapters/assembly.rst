The Metagenome Assembly Workflow
==================

Summary
-------
This workflow is developed by Brian Foster at JGI and original from his repo. It take paired-end reads runs reads quailty trimming, artifact removal, linker-trimming, adapter trimming, and spike-in/host removal by rqcfilter (BBTools:38.44), then error corrected by bbcms (BBTools). The clean reads are assembled by MetaSpades. After assembly, the reads are mapped back to contigs by bbmap (BBTools) for coverage information.

Workflow Diagram
------------------

.. image:: ../_static/images/assembly/workflow_assembly.png
   :scale: 75
   :alt: Metagenome assembly workflow dependencies


TODO: Need a Cromwell generated diagram from WDL definition of the workflow




Workflow Dependencies
---------------------
Third party software
~~~~~~~~~~~~~~~~~~~~

- conda v4.7.10 (BSD 3-Clause)
- MetaSPades v3.13.0 (GPLv2)
- BBTools:38.44 (License)

Database
~~~~~~~~
- None

Workflow Availability
---------------------
Git repo:
https://github.com/microbiomedata/WorkflowPlanning/tree/master/AssemblyPipeline
Container:


Test datasets
-------------

- Mock dataset: SRR7877884
- simulated dataset


Details
---------------------

Inputs
~~~~~~~~

Outputs
~~~~~~~~





Running Workflow in Cromwell on Cori
----------------------------
You should run this on Cori. There are three ways to run the workflow.

CromwellJtmShifter/: The Cromwell run in head node send tasks to jtm-task-managers which will manages the tasks running on a computer node and using Shifter to run applications.
SlurmCromwellShifter/: The submit script will request a node and launch the Cromwell. The Cromwell manages the workflow by using Shifter to run applications.
CromwellSlurmShifter/: The Cromwell run in head node and manages the workflow by submitting each step of workflow to compute node where applications were ran by Shifter.
Description of the files in each sub-directory:

.wdl file: the WDL file for workflow definition
.json file: the example input for the workflow
.conf file: the conf file for running Cromwell.
.sh file: the shell script for running the example workflow
The Docker image and Dockerfile can be found here
bryce911/bbtools:38.44

bryce911/spades:3.13.0

Input files

