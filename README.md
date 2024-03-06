[![Makefile CI](https://github.com/nneehhaa123/logistic_test/actions/workflows/makefile.yml/badge.svg)](https://github.com/nneehhaa123/logistic_test/actions/workflows/makefile.yml)

This Repo can be used to convert any DS project for Continuos Intergration.
- Create folder structure for Data/ Model development/ inference/ test
- create Makefile and Requiremnet file. This make file can be used to automate the steps like creating env , cleaning formating, testing and deploying the code. We can levergae this file to in github/ wrokflow later also.
- Once this repo is setup. Push the code to main/ dvelopment branch.
- After that create workflow for CI, via Actions--> New Workflow . select appropriate option or workflow in this repo can also be used where direct Run commands or make file commands can be tested. Wecan setup to run this workflow whenever there is change and new code is pushed in repo. We can have the results and model KPIs also printed as part of this run to verify and track the Model impact.
- Once the build is run succesfully, we can leverage the Docker file to create image of the project. however, this image will be saved locally. it can be pushed to Docker hub as well. Same image can be run via docker run commands. It will successfully deploy the code but app link will not work .
- This can be pushed to EXR and deploy from there via App runner
- 
