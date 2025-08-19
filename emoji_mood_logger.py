import datetime

print("📝 Mood Logger with Emojis")

mood = input("How are you feeling today? (Use emojis like 😊😢😡🤔): ")
note = input("Want to add a note? (optional): ")

entry = f"$(date +%Y-%m-%d) - Mood: ${mood} | Note: ${note}\n"

with open("mood_log.txt", "a") as file:
    file.write(entry)

print("✅ Mood saved!")
