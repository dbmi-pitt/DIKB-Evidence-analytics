##### Sam Rosko's file for running the DRIVE Empirical Experiment
##### TO DO: Test extensively
##### Last Update: 2017-03-21

from DIKB.DIKB import *
from DIKB.DrugModel import *
from DIKB.EvidenceModel import *
from DIKB.ExportAssertions import *

import os
import sys
import errno
import shutil
import time

rootdir = "/media/scr25/DATA/DRIVE-Experiment/DIKB-Evidence-analytics/Drive-Experiment/summer_experiments/experiment_colloquium/"

##### Function for easy symbolic link reassignment
def symlink_force(target, link_name):
    try:
        os.symlink(target, link_name)
    except OSError, e:
        if e.errno == errno.EEXIST:
            os.remove(link_name)
            os.symlink(target, link_name)
        else:
            raise e

##### count is used to limit number of runs... don't want to have to deal with 36,000 when building file
count = 1
##### this is used to track how long the system takes to run
startTime = time.time()

##### must set log level, can be changed
os.environ["DIKB_LOG_LEVEL"] = "2" 

##### Unpickle the KB, only needs to be done once
new_ev = EvidenceBase("evidence","test-June2015")
new_dikb = DIKB("dikb","Test 2015", new_ev)
new_dikb.unpickleKB('../dikb-pickles/dikb-test.pickle')
new_ev.unpickleKB('../dikb-pickles/ev-test.pickle')

##### Fix old bug
for e,v in new_ev.objects.iteritems():
    if v.assert_by_default == '0':
         v.assert_by_default = False
    else:
         v.assert_by_default = True
    v.ready_for_classification = True

##### Loops through all 36,000 folders
for root, dirs, files in os.walk(rootdir):   
    for name in dirs:
        
        # if count >= 6:
        #     endTime = time.time()
        #     if (endTime-startTime) > 60:
        #         print "\nEND - Time in Minutes"   
        #         print (endTime-startTime)/60
        #         sys.exit()
        #     else:
        #         print "\nEND - Time in Seconds"
        #         print (endTime-startTime)
        #         sys.exit()
        
        ##### Set the symbolic link for levels of evidence to the one in the current folder
        print(os.path.join(root, name))
        symlink_force((os.path.join(root, name)+"/levels-of-evidence"), "../data/levels-of-evidence")

        ##### Create assertions and changing_assumptions files using given evidence
        reset_evidence_rating(new_ev, new_dikb)
        exportAssertions(new_ev, new_dikb, "../assertions.lisp")
        assessBeliefCriteria(new_dikb, new_ev, "../changing_assumptions.lisp")

        ##### Open "assertions.lisp" and modify it to backslash commas and parentheses
        filein = "/media/scr25/DATA/DRIVE-Experiment/DIKB-Evidence-analytics/Drive-Experiment/assertions.lisp"        
        f = open(filein,'r')
        filedata = f.read()
        f.close()

        newdata = filedata.replace(",","\,")
        newdata = newdata.replace("-(","-\(")
        newdata = newdata.replace(")-","\)-")

        fileout = "/media/scr25/DATA/DRIVE-Experiment/DIKB-Evidence-analytics/Drive-Experiment/assertions.lisp"  
        f = open(fileout,'w')
        f.write(newdata)
        f.close()

        ##### Open "changing_assumptions.lisp" and modify it to backslash commas and parentheses
        filein = "/media/scr25/DATA/DRIVE-Experiment/DIKB-Evidence-analytics/Drive-Experiment/changing_assumptions.lisp"        
        f = open(filein,'r')
        filedata = f.read()
        f.close()

        newdata = filedata.replace(",","\,")
        newdata = newdata.replace("-(","-\(")
        newdata = newdata.replace(")-","\)-")

        fileout = "/media/scr25/DATA/DRIVE-Experiment/DIKB-Evidence-analytics/Drive-Experiment/changing_assumptions.lisp"  
        f = open(fileout,'w')
        f.write(newdata)
        f.close()

        ##### Copy edited files to the folders to maintain a copy when other is overwritten
        shutil.copy2("/media/scr25/DATA/DRIVE-Experiment/DIKB-Evidence-analytics/Drive-Experiment/assertions.lisp", (os.path.join(root, name) + "/assertions.lisp"))
        shutil.copy2("/media/scr25/DATA/DRIVE-Experiment/DIKB-Evidence-analytics/Drive-Experiment/changing_assumptions.lisp", (os.path.join(root, name) + "/changing_assumptions.lisp"))

        ##### This switches the directory temporarily so that the LISP file can be ran, then switches it back
        olddir = os.getcwd()
        newdir = "/media/scr25/DATA/DRIVE-Experiment/DIKB-Evidence-analytics/jtms/"
        os.chdir(newdir)
        os.system("sbcl --script project-class-test-experiment.lisp")
        os.chdir(olddir)

        ##### Copy inference results to experiment folder
        shutil.copy2("/media/scr25/DATA/DRIVE-Experiment/DIKB-Evidence-analytics/jtms/inference-results", (os.path.join(root, name) + "/inference-results"))

        count = count + 1

##### Reset the symbolic link to what it was before the experiment
symlink_force("../data/levels-of-evidence-most-rigourous-2015-09-20", "../data/levels-of-evidence")
##### this is used to track how long the system takes to run
endTime = time.time()
if (endTime-startTime) > 60:
    print "\nEND - Time in Minutes"   
    print (endTime-startTime)/60
else:
    print "\nEND - Time in Seconds"
    print (endTime-startTime)
