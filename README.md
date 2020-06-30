# Readme

Last update: 6/30/2020.    

This is the documenation for the NMDC workflows. The latest version of this documenation can be found from
https://github.com/microbiomedata/workflow_documentation

This documentation is written in reStructuredText with Sphinx.

To compile a PDF run this command in Terminal:

python compose.py

This command will pull down the NMDC workflows, whose repositories are defined in the nmdc_doc.yaml file. It will extract docs/*.rst files from individual workflows and put them (alone with referenced png graphics if any) into the _doc directory. The assumpution is that all NMDC workflows follows the directory conversion (/docs) for documentation and only one rst file is used.

Then go to the _doc directory and use the following commaand to generate PDF documentation:

make pdflatex    

The result pdf file is located at docs/_build/latex/NMDCWorkflows.pdf

You can also run this single command in the root directory of this repository:

      python compose.py && cd docs && make latexpdf
      


