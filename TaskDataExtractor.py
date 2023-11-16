import spacy
from spacy.matcher import Matcher

# Initialize spacy
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
# Add match patterns
PatterTask = [
    [{"LOWER": "start"}],
    [{"LOWER": "stop"}]
]

PatterTaskType = [
    [{"LOWER": "task"}, {"LOWER": "type"}],
]

PatterTime = [
[{"LOWER": "expected"},{"LOWER": "time"},{}],
[{"LOWER": "estimated"},{"LOWER": "time"},{}],
]

matcher.add("Task", PatterTask)
matcher.add("TaskType", PatterTaskType)
matcher.add("Time", PatterTime)

class TaskDataExtractor:
    def __init__(self):
        self.init()
    def init(self):
        self.TaskEnd = -1
        self.TaskTypeStart = -1
        self.TaskTypeEnd = -1
        self.TimeStart = -1
        self.TimeEnd = -1
        self.Task = ''
        self.TaskType = ''
        self.Time = ''
        
    def extract_data(self):
        # Find correct order and assign text to variables
        if 0 <= self.TimeEnd < self.TaskTypeEnd:
            self.Task = self.doc[self.TaskEnd:self.TimeStart]
            self.TaskType = self.doc[self.TaskTypeEnd:]
            self.Time = self.doc[self.TimeEnd - 1]
        elif 0 <= self.TaskTypeEnd < self.TimeEnd:
            self.Task = self.doc[self.TaskEnd:self.TaskTypeStart]
            self.TaskType = self.doc[self.TaskTypeEnd:self.TimeStart]
            self.Time = self.doc[self.TimeEnd - 1]
        elif self.TaskTypeEnd < 0 and self.TimeEnd > 0:
            self.Task = self.doc[self.TaskEnd:self.TimeStart]
            self.Time = self.doc[self.TimeEnd - 1]
        elif self.TimeEnd < 0:
            self.Task = self.doc[self.TaskEnd:self.TaskTypeStart]
            self.TaskType = self.doc[self.TaskTypeEnd:]
        else:
            self.Task = self.doc[self.TaskEnd:]
        #return self.Task, self.TaskType, self.Time
    
    def find_start_end(self, input_text):
        print(input_text)
        self.doc = nlp(input_text)
        print(self.doc)
        matches = matcher(self.doc)
        for match_id, start, end in matches:
            matched_text = self.doc[start:end].text
            string_id = nlp.vocab.strings[match_id]
            if string_id == "Task":
                self.TaskEnd = end
            elif string_id == "TaskType":
                self.TaskTypeStart = start
                self.TaskTypeEnd = end
            elif string_id == "Time":
                self.TimeStart = start
                self.TimeEnd = end
            # Debug
            print(f"Matched text: {matched_text}, Match ID: {string_id}")
            self.extract_data()