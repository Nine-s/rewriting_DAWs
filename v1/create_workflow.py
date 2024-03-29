import os
import glob
import json
from infra import Infra
import input
import infra
from DAW import DAW
from workflow_generation import workflow
from to_nextflow import to_nextflow
from annotation import AnnotationDB

annotation_files = []
annotation_path = './annotation_files'
for i in os.listdir(annotation_path):
    if (i.endswith('.json')):
        full_path = '%s/%s' % (annotation_path, i)
        annotation_files.append(full_path)
        #print(full_path)
annotDB = AnnotationDB(annotation_files)

with open('/home/simon/GitHub/rewriting_DAWs/rnasplice-description/INFRA.json') as jsonfile:
    infra_description = json.load(jsonfile)

with open('/home/simon/GitHub/rewriting_DAWs/rnasplice-description/DAW.json') as jsonfile:
    daw_description = json.load(jsonfile)

with open('/home/simon/GitHub/rewriting_DAWs/rnasplice-description/SPLIT_MERGE_TASKS.json') as jsonfile:
    split_merge_tasks = json.load(jsonfile)

with open('/home/simon/GitHub/rewriting_DAWs/rnasplice-description/INPUT_EVAL_REDUCED.json') as jsonfile:
    input_description = json.load(jsonfile)

#define objects for infra + nodes
my_infra = Infra(infra_description)

#define objects for input + reference
#my_input = input(input_description)

# define object for DAW + task + connection
my_DAW = DAW(daw_description, input_description, my_infra, annotDB)

my_DAW = my_DAW.rewrite(annotationdb=annotDB, input_description=input_description, split_merge_annotation=split_merge_tasks)

to_nextflow(my_DAW)
#to_cwl(my_DAW)

# TODO: define library of tasks Nextflow(->nfcore) / CWL find repos
