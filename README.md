## UE Projet de Fin d'Étude

Ceci represente notre livrable pour notre Projet de Fin d'Étude : __Modélisation par apprentissage du comportement verbale et non verbal d'un agent virtuel__ , plus spécifiquement de la tache  de __"Conversion de pose 2D à 3D"__.

Membres du goupe :
  - Begum Bekiroglu
  - Yasmine Djabri
  - Nacereddine LADDAOUI

---
## Intro
The main subject of this repository is to build a neural network model that predicts the upper body 3D pose from 2D pose. This work is designed to fit for ISIR's  [virtual agent](https://github.com/isir/greta).

Our work is structured as so :
- Data preparation
- Training part
- Convert the 3D pose into BVH, to feed them into the the virtual agent.


## Demo 
The provide demo script provides a real-time test of our the trained model directly from the webcam. You can run it by executing the following command :
```
./demo_webcam.py 
```

## Integration to Greta


In order to adapt the positions found to the virtual agent Greta, we have first converted the poses that we have as numpy files to .bvh files using numpy-to-bvh.py module. Then, to transform our poses so that they can be interpretable by Greta the module "fix_bvh_for_GRETA.py" in the following git can be used: https://github.com/Michele1996/PFE-OpenPose-to-VAE-to-BVH.
