# EduLite AI Benchmark Results

## Test Device

EduLite AI was tested on a budget laptop with the following specifications:

* Laptop: ASUS
* Operating system: Windows 11 Home with Ubuntu through WSL
* RAM: 8GB
* Processor: Intel Core i5
* System type: 64-bit operating system
* Graphics: Integrated graphics
* Cloud dependency: None during local inference

## Runtime

* Runtime: llama.cpp
* Model format: GGUF
* Model: Qwen2.5-1.5B-Instruct Q4_K_M
* Model file: model/qwen2.5-1.5b-instruct-q4_k_m.gguf

## Test 1: Vocabulary Builder

Prompt:

Explain the word "resilient" for a secondary school student.

Result:

The model generated pronunciation support, part of speech, simple meaning, example sentences and a practice question.

Speed:

* Prompt processing: 18.0 tokens/second
* Generation: 8.3 tokens/second

## Test 2: Essay Feedback

Prompt:

I was walking inside the dark house. I was afraid. I heard something. I ran away.

Result:

The model gave strengths, weaknesses, grammar issues and an improved version of the paragraph.

Speed:

* Prompt processing: 18.2 tokens/second
* Generation: 9.1 tokens/second

## Test 3: Teacher Feedback Mode

Prompt:

My best day was when we went to beach. I enjoy with my friends and we eat rice. It was very fun and I will never forgot it.

Result:

The model gave teacher-style feedback, identified grammar errors and rewrote the paragraph correctly.

Speed:

* Prompt processing: 19.8 tokens/second
* Generation: 9.6 tokens/second

## Summary

EduLite AI successfully ran offline on an 8GB ASUS laptop using llama.cpp and a GGUF model.

The tests show that the system can support English vocabulary learning, essay improvement and teacher-style writing feedback without cloud access.
