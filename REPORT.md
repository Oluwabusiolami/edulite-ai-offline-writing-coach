# EduLite AI: Offline English Writing Coach for African Schools

## 1. Project Summary

EduLite AI is an offline English writing assistant designed for African secondary schools. It helps students improve essays, stories, vocabulary, grammar and exam-style writing without needing internet access or cloud-based AI tools.

The project is designed for ordinary low-cost laptops, especially 8GB laptops with integrated graphics. The goal is to make AI-supported learning available in schools where internet access is unstable, expensive or unavailable.

## 2. Problem Definition

Many students in African schools need regular support with English writing. They struggle with grammar, vocabulary, essay structure, creative writing, reading responses and exam-style answers.

In many schools, teachers are responsible for large classes and may not always have enough time to give detailed feedback to every student.

Cloud-based AI tools can help, but they depend on internet access. This creates a problem in low-connectivity environments where schools may not have reliable internet, students may not have enough data, and power supply may be unstable.

EduLite AI addresses this problem by providing a local AI writing coach that can run offline on a modest laptop.

## 3. Target Users

EduLite AI is designed for:

- Secondary school students
- English learners
- Teachers
- Low-connectivity schools
- Schools using low-cost laptops
- Students preparing for English examinations

## 4. African Use Case

This project is based on real classroom needs in African schools.

Many African schools have students who need English writing support but do not always have strong internet access. EduLite AI gives such students a way to practise writing and receive feedback even when they are offline.

The tool can be used in classrooms, computer labs, hostels, libraries and homes.

## 5. What the Tool Can Do

EduLite AI supports the following learning tasks:

### Essay Correction

Students can paste an essay and receive simple feedback on grammar, vocabulary, structure and clarity.

### Creative Writing Support

Students can receive help with story planning, suspense, character development and paragraph improvement.

### Vocabulary Builder

Students can ask for the meaning, part of speech, pronunciation and example sentences for new words.

### Exam Writing Practice

Students can practise emails, articles, reports, reviews, speeches and narrative writing.

### Teacher Feedback Mode

Teachers can paste student writing and receive suggested strengths, weaknesses and improvement comments.

## 6. Model and Runtime

The planned model for this project is:

Qwen2.5-1.5B-Instruct Q4_K_M GGUF

Runtime:

llama.cpp

The model was selected because it is small enough for a budget laptop and can still provide useful writing support for English learning tasks.

## 7. Device Constraint

The project is designed for an 8GB laptop with integrated graphics and no cloud dependency.

Development device:

- Laptop: ASUS
- Operating system: Windows 11 Home
- RAM: 8GB
- Processor: Intel Core i5
- System type: 64-bit operating system

## 8. Offline Design

EduLite AI is designed to run without cloud services.

The model file is stored locally on the laptop. When the user enters a writing task, the model generates feedback directly on the device.

This means the tool can still work in classrooms where internet access is weak or unavailable.

## 9. Example Prompts

### Prompt 1

A Year 10 student in Nigeria has written a short story that lacks suspense. Give simple feedback, identify three weaknesses, and rewrite one paragraph to make it more engaging while keeping the student's voice.

### Prompt 2

Help a beginner English learner write a 150-word informal email to a friend about preparing for school examinations. Use simple vocabulary, clear paragraphs, and give five useful phrases the learner can reuse.

## 10. Expected Output Quality

EduLite AI is expected to produce:

- Clear student-friendly feedback
- Simple grammar explanations
- Improved writing samples
- Vocabulary support
- Exam-style writing guidance
- Teacher-style comments

The output is not intended to replace a teacher. It is designed to support practice, revision and classroom learning.

## 11. Why This Project Matters

EduLite AI can help reduce the gap between students who have constant access to online learning tools and students who do not.

By running offline, the tool supports digital learning in schools with limited infrastructure.

It also gives teachers a practical assistant for writing practice and student feedback.

## 12. Future Improvements

Future versions of EduLite AI could include:

- A simple desktop interface
- More African English examples
- Yoruba-supported explanations
- Pidgin-supported explanations
- More IGCSE ESL writing tasks
- Teacher dashboard
- Saved student practice records
- More local classroom datasets

## 13. Conclusion

EduLite AI shows how offline AI can support English learning in African schools.

The project focuses on practical classroom use, low-cost devices and offline access. It is a simple but useful step toward making AI learning support available to more students and teachers.
