# Intent prediction and slot filling

This was a project we had in the course *Advanced Semantic*. The project result is an end-to-end system for binary intent recognition and slot filling in the context of a dialogue system using the MultiWOZ dataset of goal-oriented dialogues (2.2). The full corpus could be accessed [here](https://github.com/budzianowski/multiwoz/tree/master/data/MultiWOZ_2.2). 

The corpus has an impressively detailed annotation involving multiple turns and multiple goals which our professor has simplified to just the initiating request (first turn) and involving two possible intents (find-hotel/find-restaurant) and the corresponding slots (name, area, parking, internet, pricerange, stars, type and food) for those intents. The data were splited into train, dev and test set, which can be found in the ./data folder in the repo.

We used logistic regression for the binary intent recognition and a combination of rule-based system and *DistilBertForQuestionAnswering* for the slot-filling task. The system achieved a **80.63%** accuracy on the dev set and a **83.75%** accuracy on the test set.

### File Directory
  * rules.py: The rules we developed for slots that can be filled using Regular Expressions. 
  * qa_sys.py: The functions for preparing the Question and Answer dataset to feed in the model.
  * intent_slot_filling.ipynb: The work flow of this project and final result.
