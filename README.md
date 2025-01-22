# Allen Brain Project - Notes, Questions, and Work Distribution

### Group Participants (in random order 🙂):
- Zoe Herzig - n12030942@students.meduniwien.ac.at 
- Jonathan Kremla - n11922635@students.meduniwien.ac.at 
- Paul Johannes Eder - n12035372@students.meduniwien.ac.at 
- Klaus Hartmann-Baruffi - n09027721@students.meduniwien.ac.at 
- Isabella Deak - n11910517@students.meduniwien.ac.at 
- Leonie Sophie Gadner - n11935308@students.meduniwien.ac.at 

### Technical setup

We created separate branches for our contributions to ensure a safe and controlled merging of changed and added code.
we created seperate branches in the github repo to seperate our concurrent coding.
So far there are 5 branches (additional to the "main"-branch, corresponding to the forenames of our group members):
- jonathan
- klaus
- leonie
- paul
- zoe 

### Websources
- our github-repo (repo-owner Evgenii): <https://github.com/EugOT/CN-pr-Allen-Brain>
- scientific paper our work is based on: “Visual Behavior 2P dataset (image change detection task)”
 Websource: <https://portal.brain-map.org/circuits-behavior/visual-behavior-2p>
- source of the dataset: <https://ndownloader.figshare.com/files/28470255/allen_visual_behavior_2p_change_detection_familiar_novel_image_sets.parquet>
- YT-Tutorial for the “Two-Photon-Dataset” from "Allen Institute": <https://www.youtube.com/watch?v=dO99XLlHA90>
- documentation of the setup: <https://allensdk.readthedocs.io/en/latest/visual_behavior_optical_physiology.html#photon-imaging-during-behavior>

## Description of our approach ("project journal")
---
#### Tue, 14th Jan:
- generating a google doc file for collaborating and brainstorming of first ideas for tasks and division of the work packages across team members
- registration and setting of permissions for the group members to github repo <https://github.com/EugOT/CN-pr-Allen-Brain>
- organization of a zoom conference to discuss tasks and aims of project with all team members
#### Thu, 16th Jan:
- zoom web meeting with discussion about the parquet dataset, useable columns/features 
#### Fri, 17th Jan:
- discussion about quality and features of the 16 images used in the experimental setup, found possible classifications as:  
   - animal/no animal
   - landscape/close up
- dropping of columns:
    - imaging_depth
    - targeted structure
    - sex
    - age_in_days
- adding of labels:
    - animal/landscape
    - close proximity/landscape
- creation of boxplots, scatter plots and pairplots to get a first insight into data quality and patterns.
#### Sun, 19th Jan:
- made dataset (with dropped and added features/columns) available as CSV file
- CSV **not possible to upload in github repo !** because of size (> 300MB), so added to .gitignore
#### Mon, 20th Jan:
- linear regression:
    - for animal (yes/no)
    - for proximity (far/close)
    - function created for grouping of neurones data with the new labels (animal, proximity) as base for linear regression
- MLP (multi layer perceptron/ neural network) for animal yes/no task
    - input neurons: dilation, speed, response, traces(?)
    - output neuron: ....
- Autoencoder + Logistic Regression (in "neural_data_analysis.ipynb"):
    - created feature vector: consists of traces 
    - label vector: animal_in_image / animal_in_image + close_proximity
    - used logistic regression in latent space
