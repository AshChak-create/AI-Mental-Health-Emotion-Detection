# AI-Powered Mental Health Support System
### Text-Based Emotion Recognition and Emotion-Aware Journaling

*An early implementation developed alongside research on multimodal emotion detection and mental health support.*

---

## Overview

Understanding how someone feels through written language is not always straightforward. A single sentence may express frustration, sadness, uncertainty, or several emotions at once. This was one of the questions that motivated my work on emotion-aware mental health support systems.

This repository contains an initial text-based prototype developed alongside my research paper, **"An AI-Powered Mental Health Support System: A Multi-Modal Approach to Emotion Detection and Crisis Intervention."**

The current implementation uses a pretrained RoBERTa model fine-tuned on the GoEmotions dataset to identify emotions expressed in text. I also developed a simple journaling interface where users can enter their thoughts, receive predicted emotion labels, and store entries locally.

The broader research explores how text and speech processing, emotion classification, adaptive responses, and crisis intervention could be brought together in a single system. This repository represents an early step toward that architecture rather than a completed multimodal application.

## Research Motivation

Emotion recognition is more complex than identifying whether a statement is positive or negative.

For instance, a person may express nervousness and excitement simultaneously, or describe a difficult experience without explicitly naming their emotions. Recognizing these distinctions is one of the challenges in building systems that respond appropriately to human communication.

My interest was in exploring how pretrained language models could support fine-grained emotion recognition and how their predictions could be integrated into a simple interactive application.

This prototype provided an opportunity to work with transformer-based models, examine emotion scores, and explore how emotion recognition might contribute to a larger mental health support framework.

## Implementation

The current project focuses on two components.

### 1. Text-Based Emotion Detection

The `main.py` script uses the Hugging Face Transformers library and the `SamLowe/roberta-base-go_emotions` model.

The implementation:

- Accepts text as input.
- Generates predictions across the GoEmotions emotion categories.
- Displays the predicted emotion labels and their associated scores.
- Includes sample sentences for testing different emotional expressions.

The model is pretrained and fine-tuned by its original developers. This project uses the available checkpoint for inference rather than training a new model.

### 2. Emotion-Aware Journaling

The `journal.py` script extends emotion detection into a basic command-line journaling application.

Users can write a journal entry, after which the model returns the three highest-scoring emotion labels.

The application saves the following information in a local CSV file:

- Date and time
- Journal entry
- Predicted emotion labels

The journaling component is an experimental demonstration of how emotion recognition could be integrated into a user-facing application. It is not intended to assess psychological conditions or provide clinical guidance.

## Dataset and Exploratory Analysis

The project draws on **GoEmotions**, a dataset introduced by Demszky et al. (2020), containing approximately 58,000 Reddit comments annotated with 27 emotion categories and a neutral category.

During the project, I also explored the GoEmotions dataset and its annotation structure using the original Google Research analysis materials.

The repository includes four figures associated with this exploratory

### Associated Research

**An AI-Powered Mental Health Support System: A Multi-Modal Approach to Emotion Detection and Crisis Intervention**

Ashmita Chakrabarty, Riddhi Panchal, Sachin Naik, and Raja Bhavani

Presented at SSIC 2025; publication in Springer proceedings in progress.

This repository contains an early text-based emotion recognition and journaling prototype developed alongside the broader research. The complete paper proposes additional components for speech processing, multimodal analysis, adaptive responses, and crisis intervention that are not implemented in this repository.