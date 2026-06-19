# EduLite AI: Offline English Writing Coach for African Schools

EduLite AI is an offline English writing assistant designed for African secondary schools where internet access, electricity and high-performance devices may be limited.

The project helps students practise English writing without needing cloud services, internet access or expensive computers. It is designed to run on an ordinary 8GB laptop using a small local language model.

## Problem

Many African students need support with English writing, grammar, vocabulary and exam-style responses. However, many schools and homes do not always have reliable internet access or powerful computers.

Most AI tools depend on the cloud. This makes them difficult to use in low-connectivity school environments.

EduLite AI solves this by providing an offline writing coach that can support students and teachers locally.

## What EduLite AI Can Do

EduLite AI can help with:

- Essay correction
- Creative writing improvement
- Grammar explanations
- Vocabulary building
- IGCSE ESL writing practice
- Simple feedback for students
- Teacher-style comments on student writing

## Target Users

EduLite AI is designed for:

- Secondary school students
- English learners
- Teachers
- Schools with limited internet access
- African classrooms using low-cost laptops

## African Use Case

This project is built around real classroom needs in African schools. It focuses on students who may not always have internet access but still need writing support, exam preparation and English language practice.

## Example Use Cases

### 1. Improve My Essay

A student pastes an essay and EduLite AI gives feedback, identifies mistakes and suggests improvements.

### 2. Story Helper

A student gives a story topic and EduLite AI helps with plot, suspense, characters and better vocabulary.

### 3. IGCSE ESL Writing Practice

A student practises email writing, article writing, reports, reviews and speeches.

### 4. Vocabulary Builder

EduLite AI explains words using meaning, part of speech, pronunciation and example sentences.

### 5. Teacher Feedback Mode

A teacher pastes a student’s writing and EduLite AI provides strengths, weaknesses and improvement advice.

## Technical Approach

EduLite AI uses a small quantized GGUF language model running locally through llama.cpp.

The goal is to keep the tool lightweight enough for an 8GB laptop while still providing useful writing support.

## Model

Planned model:

Qwen2.5-1.5B-Instruct Q4_K_M GGUF

Runtime:

llama.cpp

## Why This Matters

EduLite AI can help make AI learning support more accessible to students and teachers in schools where internet access is unstable or unaffordable.

The project shows how offline AI can be used practically in African education.

## How to Run EduLite AI

After cloning the repository, download the model:

```bash
chmod +x download_model.sh
./download_model.sh
