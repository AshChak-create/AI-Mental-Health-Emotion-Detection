import csv
import os
from datetime import datetime
from transformers import pipeline

# Load the model
classifier = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions", top_k=3)

def detect_emotions(text):
    result = classifier(text)
    return [emotion["label"] for emotion in result[0]]

# Setup log file
log_file = "logs/journal_log.csv"

# Create CSV if it doesn't exist
if not os.path.exists(log_file):
    with open(log_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["DateTime", "Journal Entry", "Top Emotions"])

def log_journal_entry():
    entry = input("📝 How are you feeling today?\n\nWrite here: ")

    emotions = detect_emotions(entry)
    emotion_str = ", ".join(emotions)

    # Save to CSV
    with open(log_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), entry, emotion_str])

    print("\n💬 Detected Emotions:")
    for emotion in emotions:
        print(f"- {emotion}")
    print("\n✅ Your journal entry has been saved!")

if __name__ == "__main__":
    log_journal_entry()
