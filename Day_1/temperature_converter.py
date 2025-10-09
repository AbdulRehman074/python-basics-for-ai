# 🌡️ Temperature Converter
# Converts between Celsius and Fahrenheit
# Author: Abdulrehman | AI Developer in Progress

print("=" * 50)
print("🔥 WELCOME TO TEMPERATURE CONVERTER 🔥".center(50))
print("=" * 50)

while True:
    print("\nChoose conversion type:")
    print("  🌡️ Type 'C' → Celsius ➜ Fahrenheit")
    print("  ❄️ Type 'F' → Fahrenheit ➜ Celsius")

    choice = input("\nEnter your choice (C/F): ").strip().upper()

    if choice == "F":
        try:
            temp_celsius = float(input("Enter temperature in Celsius (°C): "))
            temp_fahrenheit = (temp_celsius * 9 / 5) + 32
            print(f"✅ {temp_celsius:.2f}°C = {temp_fahrenheit:.2f}°F")
        except ValueError:
            print("⚠️ Invalid number! Please enter a valid temperature.")

    elif choice == "C":
        try:
            temp_fahrenheit = float(input("Enter temperature in Fahrenheit (°F): "))
            temp_celsius = (temp_fahrenheit - 32) * 5 / 9
            print(f"✅ {temp_fahrenheit:.2f}°F = {temp_celsius:.2f}°C")
        except ValueError:
            print("⚠️ Invalid number! Please enter a valid temperature.")

    else:
        print("❌ Invalid input! Please enter 'C' or 'F'.")

    # Ask if the user wants to continue
    again = input("\n🔁 Do you want to convert again? (y/n): ").strip().lower()
    if again != "y":
        print("\n👋 Goodbye, AI Developer! Keep coding smart 💡")
        print("=" * 50)
        break
