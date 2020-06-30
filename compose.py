"""
Compose documentation for NMDC workflows
"""
import os
import sys
from shutil import copy2

from git import Repo
from git.exc import GitCommandError

import yaml

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


class NMDC_Composer:
    """NMDC Composer provides an interface to NMDC resources."""
    def __init__(self, config):
        self.__version__ = 0.1
        config = yaml.load(config, Loader=Loader)
        self.ROOT_DIR = os.path.abspath(config["root_dir"])
        self.DOC_DIR = os.path.join(self.ROOT_DIR, "docs")
        self.DOC_CHAPTER_DIR = os.path.join(self.DOC_DIR, "chapters")
        self.DOC_IMG_DIR = os.path.join(self.DOC_DIR, "_static/images")
        self.WORKFLOW_DIR = os.path.join(self.ROOT_DIR, "workflows")
        self.WORKFLOWS = config["workflows"]
        self.DOCUMENTATION_TEMPLATE_REPO = config["documentation_template_repo"]

    def get_workflow_dir(self, workflow):
        """Get the absolute path of the local workflow repo"""
        try:
            assert workflow in self.WORKFLOWS.keys()
        except AssertionError:
            sys.stderr.write("{} is not a valid workflow".format(workflow))
            sys.exit()
        return (os.path.join(self.WORKFLOW_DIR, workflow))

    def checkout_documentation_template(self):
        remote_repo = self.DOCUMENTATION_TEMPLATE_REPO
        local_repo = self.DOC_DIR
        try:
            Repo.clone_from(remote_repo, local_repo)
        except GitCommandError as error:
            if error.status == 128:     # git destination path exist error
                msg = "Using existing template."
                print(msg)
                # FIXME do a git checkout instead to update it
            else:
                msg = "Error in fectching documentation template repository.\n"
                msg += " ".join(error.command)
                msg += error.stderr
                sys.exit(msg)

    def checkout_workflow_repo(self, workflow):
        """Clone a workflow module from repo."""
        try:
            assert workflow in self.WORKFLOWS.keys()
        except AssertionError:
            sys.stderr.write("{} is not a valid workflow".format(workflow))
            sys.exit()

        remote_repo = self.WORKFLOWS[workflow]
        local_repo = self.get_workflow_dir(workflow)
        try:
            Repo.clone_from(remote_repo, local_repo)
        except GitCommandError as error:
            if error.status == 128:     # git destination path exist error
                msg = 'Using existing module {}.'.format(workflow)
                print(msg)
                # FIXME do a git checkout instead to update it
            else:
                msg = ' '.join(error.command)
                msg += error.stderr
                sys.exit('Error in running git: {}'.format(msg))

    def checkout_all_workflows(self, verbose=False):
        for workflow in self.WORKFLOWS.keys():
            if verbose:
                print("Check out workflow {}".format(workflow))
            self.checkout_workflow_repo(workflow)

    def build_documentation(self, verbose=False):
        """
        Build documentation from each module's doc directory.
        0. Check out the documenation template repository
        1. Check out the repo of individual workflows
        2. Read, update, write rst files from workflow "docs" to "chapters"
        3. Add workflow names before rst files
        4. Check figures
        5. Update index.rst to include all chapter files
        """
        self.checkout_documentation_template()
        chapters = []
        for workflow in self.WORKFLOWS.keys():
            self.checkout_workflow_repo(workflow)
            local_repo = self.get_workflow_dir(workflow)
            src_dir = os.path.join(local_repo, 'docs')
            if not os.access(src_dir, os.W_OK):
                sys.stderr.write("Cannot read from {}".format(src_dir))
            for f in os.listdir(src_dir):
                if f.endswith(".rst"):
                    src = os.path.join(src_dir, f)
                    tgt = "_".join([workflow, f])
                    chapters.append(tgt)
                    tgt = os.path.join(self.DOC_CHAPTER_DIR, tgt)
                    if verbose:
                        print("Updating {} to {}".format(src, tgt))

                    if not os.access(src, os.R_OK):
                        sys.exit('Cannot open rst file {}'.format(src))

                    with open(src, 'r') as fh:
                        contents = fh.readlines()
                        for i, l in enumerate(contents):
                            if ".. image:: " in l:
                                src_img_f = l.split("image:: ")[1].strip()
                                tgt_img_f = "_".join([workflow, src_img_f])
                                tgt_img_ref = os.path.join("../_static/images/", tgt_img_f)
                                tgt_img_f = os.path.join(self.DOC_IMG_DIR, tgt_img_f)
                                contents[i] = ".. image:: {}\n".format(tgt_img_ref)
                                copy2(os.path.join(src_dir, src_img_f), tgt_img_f)
                        with open(tgt, 'w') as fh:
                            fh.writelines(contents)
        self.write_index_rst(chapters)
        print("Run this command to generate docs/_build/latex/NMDCWorkflows.pdf: cd docs&&make latexpdf")



    def write_index_rst(self, chapters):
        """Add index.rst """
        index_rst = os.path.join(self.DOC_DIR, 'index.rst')
        if not os.access(index_rst, os.W_OK):
            sys.exit('Cannot write to {}'.format(index_rst))
        with open(index_rst, 'w') as rst:
            rst.write("""
Welcome to NMDC Workflows's documentation!
==========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   chapters/overview.rst
""")
            for chapter in chapters:
                rst.write("   chapters/{}\n".format(chapter))


if __name__ == '__main__':
    config = "nmdc_doc.yaml"
    with open(config, "r") as config:
        manager = NMDC_Composer(config)
        manager.build_documentation(verbose=False)
