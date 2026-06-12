from classifier import classify_message
from templates import build_message
from tts import speak

def main():
    user = input("Usuário: ")
    message = input("Mensagem: ")

    category = classify_message(message)

    final_message = build_message(
        user,
        message,
        category
    )

    print("\n===== RESULTADO =====")
    print(f"Categoria: {category}")
    print(final_message)

    speak(final_message)

if __name__ == "__main__":
    main()