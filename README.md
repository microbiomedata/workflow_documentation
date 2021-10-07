# NMDC Workflow Documentation

Last update: 10/7/2021.

This is the documenation for the NMDC workflows. The latest version of this documenation can be found from [here.](
https://github.com/microbiomedata/workflow_documentation)

This documentation is written in reStructuredText with Sphinx. It can be compiled to PDF, HTML and other formats.

    
## How to use this tool
To compile a PDF run this command in Terminal:

    `python compose.py`

This command will pull down the NMDC workflows, whose repositories are defined in the nmdc_doc.yaml file. It will extract docs/*.rst files from individual workflows and put them (alone with referenced png graphics if any) into the _doc directory. The assumpution is that all NMDC workflows follows the directory conversion (/docs) for documentation and only one rst file is used.

## Make PDF documentation    

Then go to the _doc directory and use the following commaand to generate PDF documentation:

make pdflatex    

The result pdf file is located at docs/_build/latex/NMDCWorkflows.pdf

You can also run this single command in the root directory of this repository:

      `python compose.py && cd docs && make latexpdf`

## Make Read The Doc HTML documentation
    
You can also run this single command in the root directory of this repository:

      `python compose.py && cd docs && make html`

An on-line version of the documentation is available [here](https://nmdc-workflow-documentation.readthedocs.io/en/latest/index.html).

## How to add a new workflow documentation

    New workflow documentations can be added easily by editing the "nmdc_doc.yaml" file. For example to add the metaproteomics workflow documentation, one just need to add the follolwing line under the *workflow* section:
    '5_Metaproteomics': 'https://github.com/microbiomedata/metaPro'

    Note that the first item is the workflow name the value string after it is URL to the repository of this workflow. 

    The workflows section now looks like this:
    '1_RQC': 'https://github.com/microbiomedata/ReadsQC'
    '2_MAG': 'https://github.com/microbiomedata/metaMAGs.git'
    '3_MetaGAssemly': 'https://github.com/microbiomedata/metaAssembly.git'
    '4_MetaGAnnotation': 'https://github.com/microbiomedata/mg_annotation.git'
    '5_Metaproteomics': 'https://github.com/microbiomedata/metaPro'    


      


