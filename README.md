# AI-HandsOn

#### AI: Is a system that can imitate human behavior
#### ML: Developing a system that can learn and adapt without human intervention
#### Data science: Is a field that attempts to find patterns and draw insight from data 
#### Deep Learning: Used to build a learning algorithm that mimics the human brain. Motivation behind DL is the biological Neuron (Perceptron)
- Dendrite: Receives signal from other neurons
- Cell body: Sum all inputs
- Axon: It is used to transmit signals to other cells

#### Tensorflow Google library used for deep learning - Google Lens applies deep learning image processing

#### ML Types:
-  Supervised ML: Use labeled input (input contains output label) to train the model and learn the output
-  Unsupervised ML: Use unlabeled data to learn about the patterns in the data
-  Reinforcement ML: Agent learning in an interactive environment based on rewards and penalties

#### Input^n (Feature) -> Model -> Output
#### Feature: 
-  Qualitative: Categorical data (finite number of categories)
-    Nominal data (No inherent order) -> One hot encoding (1 if match category else 0), e.g: "name of countries" [USA, AFG, IND] | input => "AFG" => [0,1,0]
-    Ordinal data (Inherent order) -> data have a relationship to each other, e.g: [poor, good, very good, excellent] - you can mark these data with a number like 1-5
-  Quantitative: Numerical valued data (discrete or continuous)

#### Supervised Tasks: 
-  Classification - predict discrete classes, e.g: [pizza, hotDog, iceCream]
-    MultiClass Classification - each of the above item
-    Binary Classification - hotDog or non-hotDog another e.g (spam/not spam)
-  Regression - predict continuous value


#### Training model
-  Training dataset | Validation dataset | Testing dataset
-  Training dataset => model => output vs actual-data = loss (make adjustment or training to get output closer to the actual data)
-  Validation set => model => output vs actual-data = loss (Validation set used as reality check during or after training to ensure the model can handle unseen data)

#### ML sample dataset 
-  https://archive.ics.uci.edu
#### Training model exercise colab
- https://colab.research.google.com/drive/1xjPZDKHUXGWfaa9Rb5sOBMdaBiMPxVtq#scrollTo=G1GwzdsGQ8px 

#### K-nearest neighbors (KNN)
- In an example of having a dataset of kids' income, with (+) or without (-) a car, if we encounter (*) a new label, the KNN will take the label from its nearest data.
- Euclidean distance - A straight line distance of (*) from other labels (- or +) - d = ^/"""""" (x1-x2)^2 + (y1-y2)^2 """"""
- K represents the number of nearest distances, e.g, 3 - we take the 3 nearest labels to predict whether the label should be (- or +)



















Reference
  -  Promping Guide - [Link](https://www.promptingguide.ai)
  -  Techno Sapien - [Link](https://technosapien.substack.com/)
  -  Second Brain - [Link](https://technosapien.substack.com/p/how-to-build-a-second-brain)
  -  Taking notes - [Link](https://obsidian.rocks/getting-started-with-zettelkasten-in-obsidian/)
