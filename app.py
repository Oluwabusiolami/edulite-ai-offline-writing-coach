import os
import subprocess
import shutil

MODEL_PATH = "model/qwen2.5-1.5b-instruct-q4_k_m.gguf"

SYSTEM_PROMPT = """
You are EduLite AI, an offline English writing coach for African secondary schools.
Help students improve essays, grammar, vocabulary, creative writing and exam-style English responses.
Use simple, clear and encouraging language.
Do not replace the teacher. Support learning and revision.
"""

def find_llama_cli():
    possible_commands = [
        os.environ.get("LLAMA_CLI"),
        "llama-cli",
        "main",
        "llama.cpp/build/bin/llama-cli",
        "llama.cpp/build/bin/Release/llama-cli.exe",
        "llama.cpp/build/bin/Debug/llama-cli.exe"
    ]

    for command in possible_commands:
        if not command:
            continue

        if os.path.exists(command):
            return command

        found = shutil.which(command)
        if found:
            return found

    return None


def build_prompt(user_prompt):
    return f"""<|im_start|>system
{SYSTEM_PROMPT}
<|im_end|>
<|im_start|>user
{user_prompt}
<|im_end|>
<|im_start|>assistant
"""


def run_edulite(user_prompt):
    llama_cli = find_llama_cli()

    if llama_cli is None:
        print("\nERROR: llama.cpp was not found.")
        print("Please install llama.cpp and make sure llama-cli is available.")
        print("You can also set the LLAMA_CLI environment variable to the path of llama-cli.")
        return

    if not os.path.exists(MODEL_PATH):
        print("\nERROR: Model file was not found.")
        print(f"Expected model path: {MODEL_PATH}")
        print("Please run download_model.sh first.")
        return

    prompt = build_prompt(user_prompt)

    command = [
        llama_cli,
        "-m", MODEL_PATH,
        "-p", prompt,
        "-n", "400",
        "--temp", "0.7"
    ]

    print("\nEduLite AI is thinking...\n")

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print("\nAn error occurred while running the model.")


def main():
    print("=" * 60)
    print("EduLite AI: Offline English Writing Coach")
    print("=" * 60)
    print("Choose a mode:")
    print("1. Essay Feedback")
    print("2. Creative Writing Helper")
    print("3. Vocabulary Builder")
    print("4. IGCSE ESL Writing Practice")
    print("5. Teacher Feedback Mode")
    print("6. Custom Prompt")

    choice = input("\nEnter a number from 1 to 6: ").strip()

    if choice == "1":
        user_prompt = input("\nPaste the student's essay or paragraph:\n")
        prompt = f"Give simple essay feedback for this student writing. Identify strengths, weaknesses, grammar issues and suggest an improved version:\n\n{user_prompt}"

    elif choice == "2":
        user_prompt = input("\nEnter the story title or idea:\n")
        prompt = f"Help a secondary school student plan a creative story on this topic. Include plot, characters, suspense and useful vocabulary:\n\n{user_prompt}"

    elif choice == "3":
        user_prompt = input("\nEnter the word:\n")
        prompt = f"Explain this word for a secondary school student. Include pronunciation, part of speech, simple meaning, two example sentences and one practice question:\n\n{user_prompt}"

    elif choice == "4":
        user_prompt = input("\nEnter the writing task:\n")
        prompt = f"Help a beginner English learner complete this IGCSE-style writing task. Give structure, useful phrases and a sample answer:\n\n{user_prompt}"

    elif choice == "5":
        user_prompt = input("\nPaste the student's writing:\n")
        prompt = f"Act as a supportive English teacher. Give teacher-style feedback, identify grammar mistakes and rewrite the student's paragraph correctly:\n\n{user_prompt}"

    else:
        prompt = input("\nEnter your prompt:\n")

    run_edulite(prompt)


if __name__ == "__main__":
    main()
