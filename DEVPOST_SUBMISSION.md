# EduLite AI Devpost Submission

## Project Name

EduLite AI: Offline English Writing Coach for African Schools

## Short Description

EduLite AI is an offline English writing coach that helps African secondary school students improve essays, grammar, vocabulary, creative writing and exam-style responses on an ordinary 8GB laptop without internet access.

## Inspiration

Many students in African schools need support with English writing, but not every school has reliable internet access or powerful computers. Most AI tools depend on the cloud, which makes them difficult to use in low-connectivity classrooms.

EduLite AI was inspired by the need to make AI learning support available to students and teachers even when there is no internet connection.

## What It Does

EduLite AI helps students and teachers with:

* Essay feedback
* Creative writing support
* Vocabulary building
* IGCSE ESL writing practice
* Grammar correction
* Teacher-style feedback on student writing

## How It Works

EduLite AI runs locally on a laptop using a small GGUF language model through llama.cpp.

The user opens the app, chooses a mode, enters a writing task or student paragraph, and receives feedback directly from the local model. No cloud service is required during inference.

## Built With

* Python
* llama.cpp
* GGUF model format
* Qwen2.5-1.5B-Instruct Q4_K_M
* Ubuntu through WSL on Windows 11
* GitHub

## African Use Case

EduLite AI is designed for African classrooms where internet access, electricity and high-performance devices may be limited.

It can support schools, computer labs, hostels, libraries and homes by giving students a way to practise English writing offline.

## Testing

EduLite AI was tested offline on an ASUS 8GB laptop.

Recorded local generation speeds:

* Vocabulary Builder: 8.3 tokens/second
* Essay Feedback: 9.1 tokens/second
* Teacher Feedback Mode: 9.6 tokens/second

## Challenges

The main challenge was getting a useful language model to run on a modest 8GB laptop without cloud dependency.

Another challenge was setting up Ubuntu through WSL and installing the local runtime tools.

## Accomplishments

EduLite AI successfully ran offline on a budget laptop.

It produced vocabulary explanations, essay feedback and teacher-style corrections without using cloud AI services.

## What Is Next

Future improvements could include:

* A simple desktop interface
* More African English examples
* Yoruba-supported explanations
* Pidgin-supported explanations
* More IGCSE ESL writing tasks
* Saved student practice records
* Teacher dashboard
