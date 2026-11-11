from transformers import pipeline

# Load the GoEmotions model from Hugging Face
classifier = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions", top_k= None)

def detect_emotions(user_text):
    print(f"\nAnalyzing emotions for: \"{user_text}\"\n")
    results = classifier(user_text)
    for emotion in results[0]:  # because results is a list of lists
        print(f"Emotion: {emotion['label']}, Confidence: {round(emotion['score'] * 100, 2)}%")

# Direct test
results = classifier("I feel so stressed and overwhelmed with everything lately.")
for emotion in results[0]:
    print(f"{emotion['label']} → {round(emotion['score'] * 100, 2)}%")

# Test cases
if __name__ == "__main__":
    detect_emotions("I'm feeling very anxious and alone lately.")
    detect_emotions("I am excited about my new project and full of energy!")
