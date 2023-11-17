# LazyVoiceAssistant
## Desclimer
LazyVoiceAssistant is in the early stages of development, and I work on it sporadically during my free time. Speech-to-text is not perfect and sometimes it's drunk. Accuracy can be improved by sacrificing time and space, to do that go to micrphone_recognition_gpu.py and change self.whisperModel to bigger models.

## Usage
run with:
```bash
python3 ./main.py
```
### Wakeword
"Alexa"

### Commands
Save new worklog entry
- Save [...] task type [...] estimatied|expected time [number];
- Save [...] estimatied|expected time [number] task type [...];
- Save [...] estimatied|expected time [number];
- Save [...] task type [...];
- Save [...];

### Planned features:
- Command for stoping the previous task and adding actual time with ability to add notes,
- Gui,
- Improved code flexibility,
- Improvement in intent recognition and speech-to-text

Feel free to contribute to the code :).