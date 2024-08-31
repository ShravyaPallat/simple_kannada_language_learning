import random

# Recreating the initial part of the list since the variable 'kannada_words' is undefined now.

words = [
    {"Kannada": "ನಮಸ್ಕಾರ", "Romanized": "Namaskara", "English": "Hello"},
    {"Kannada": "ಹೌದು", "Romanized": "Howdu", "English": "Yes"},
    {"Kannada": "ಇಲ್ಲ", "Romanized": "Illaa", "English": "No"},
    {"Kannada": "ದಯವಿಟ್ಟು", "Romanized": "Dayavittu", "English": "Please"},
    {"Kannada": "ಧನ್ಯವಾದಗಳು", "Romanized": "Dhanyavadagalu", "English": "Thank you"},
    {"Kannada": "ಕ್ಷಮಿಸಿ", "Romanized": "Kshamisi", "English": "Sorry"},
    {"Kannada": "ಬರೇನು", "Romanized": "Barenu", "English": "What"},
    {"Kannada": "ಹೇಗಿದೆ", "Romanized": "Hegide", "English": "How"},
    {"Kannada": "ಹೆಸರು", "Romanized": "Hesaru", "English": "Name"},
    {"Kannada": "ಮನೆ", "Romanized": "Mane", "English": "House"},
    {"Kannada": "ನಾನು", "Romanized": "Naanu", "English": "I"},
    {"Kannada": "ನೀವು", "Romanized": "Neewu", "English": "You"},
    {"Kannada": "ಅವರು", "Romanized": "Avaru", "English": "They"},
    {"Kannada": "ಮಗ", "Romanized": "Maga", "English": "Son"},
    {"Kannada": "ಮಗಳು", "Romanized": "Magalu", "English": "Daughter"},
    {"Kannada": "ಅಮ್ಮ", "Romanized": "Amma", "English": "Mother"},
    {"Kannada": "ಅಪ್ಪ", "Romanized": "Appa", "English": "Father"},
    {"Kannada": "ಹೆಂಡತಿ", "Romanized": "Hendati", "English": "Wife"},
    {"Kannada": "ಗಂಡ", "Romanized": "Ganda", "English": "Husband"},
    {"Kannada": "ಊಟ", "Romanized": "Oota", "English": "Food"},
    {"Kannada": "ಬಿಸಿಲು", "Romanized": "Bisilu", "English": "Sun"},
    {"Kannada": "ಮಳೆ", "Romanized": "Male", "English": "Rain"},
    {"Kannada": "ಆಕಾಶ", "Romanized": "Aakasha", "English": "Sky"},
    {"Kannada": "ನೀರು", "Romanized": "Neeru", "English": "Water"},
    {"Kannada": "ಬೆಳ್ಳಿ", "Romanized": "Belli", "English": "Silver"},
    {"Kannada": "ಮೊಳಕೆ", "Romanized": "Molake", "English": "Root"},
    {"Kannada": "ಮಣ್ಣು", "Romanized": "Mannu", "English": "Soil"},
    {"Kannada": "ಹೂ", "Romanized": "Hoo", "English": "Flower"},
    {"Kannada": "ಹಣ್ಣು", "Romanized": "Hannu", "English": "Fruit"},
    {"Kannada": "ಗಿಡ", "Romanized": "Gida", "English": "Plant"},
    {"Kannada": "ಮರ", "Romanized": "Mara", "English": "Tree"},
    {"Kannada": "ಮಗು", "Romanized": "Magu", "English": "Child"},
    {"Kannada": "ಬೆಳಕು", "Romanized": "Belaku", "English": "Light"},
    {"Kannada": "ಕತ್ತಲು", "Romanized": "Kattalu", "English": "Darkness"},
    {"Kannada": "ಊರು", "Romanized": "Uru", "English": "Village"},
    {"Kannada": "ಮನೆ", "Romanized": "Mane", "English": "Home"},
    {"Kannada": "ಬೆಳಗುವ", "Romanized": "Belaguvanu", "English": "Morning"},
    {"Kannada": "ರಾತ್ರಿ", "Romanized": "Ratri", "English": "Night"},
    {"Kannada": "ಸಿಹಿ", "Romanized": "Sihi", "English": "Sweet"},
    {"Kannada": "ಹುಳಿ", "Romanized": "Huli", "English": "Sour"},
    {"Kannada": "ಹಲಸು", "Romanized": "Halasina", "English": "Jackfruit"},
    {"Kannada": "ಎತ್ತರ", "Romanized": "Ettara", "English": "Height"},
    {"Kannada": "ಆಹಾರ", "Romanized": "Aahaara", "English": "Meal"},
    {"Kannada": "ಪರಿಸರ", "Romanized": "Parisara", "English": "Environment"},
    {"Kannada": "ಸಮುದ್ರ", "Romanized": "Samudra", "English": "Ocean"},
    {"Kannada": "ನದಿ", "Romanized": "Nadi", "English": "River"},
    {"Kannada": "ಕಡಲು", "Romanized": "Kadalu", "English": "Sea"},
    {"Kannada": "ಪಶು", "Romanized": "Pashu", "English": "Animal"},
    {"Kannada": "ಹುಲಿ", "Romanized": "Huli", "English": "Tiger"},
    {"Kannada": "ಸಿಂಹ", "Romanized": "Simha", "English": "Lion"},
    {"Kannada": "ಅನಿಲ", "Romanized": "Anila", "English": "Wind"},
    {"Kannada": "ಗಾಳಿ", "Romanized": "Gali", "English": "Air"},
    {"Kannada": "ನಿಲ್ದಾಣ", "Romanized": "Nildana", "English": "Station"},
    {"Kannada": "ಬಸ್", "Romanized": "Bas", "English": "Bus"},
    {"Kannada": "ರೇಲು", "Romanized": "Rhelu", "English": "Train"},
    {"Kannada": "ಹಡಗು", "Romanized": "Hadagu", "English": "Ship"},
    {"Kannada": "ಪದ", "Romanized": "Pada", "English": "Word"},
    {"Kannada": "ಗ್ರಂಥ", "Romanized": "Granthha", "English": "Book"},
    {"Kannada": "ಅಕ್ಷರ", "Romanized": "Akshara", "English": "Letter"},
    {"Kannada": "ಮೇಜು", "Romanized": "Meju", "English": "Table"},
    {"Kannada": "ಕಿಟಕಿ", "Romanized": "Kitaki", "English": "Window"},
    {"Kannada": "ಬಾಗಿಲು", "Romanized": "Bagilu", "English": "Door"},
    {"Kannada": "ನೆನಪು", "Romanized": "Nenapu", "English": "Memory"},
    {"Kannada": "ಸ್ನೇಹ", "Romanized": "Sneha", "English": "Friendship"},
    {"Kannada": "ವಿಶ್ವಾಸ", "Romanized": "Vishwasa", "English": "Trust"},
    {"Kannada": "ಭಯ", "Romanized": "Bhaya", "English": "Fear"},
    {"Kannada": "ಹಗಲು", "Romanized": "Hagalu", "English": "Day"},
    {"Kannada": "ಹೊಸ", "Romanized": "Hosa", "English": "New"},
    {"Kannada": "ಹಳೆ", "Romanized": "Hale", "English": "Old"},
    {"Kannada": "ದೊಡ್ಡ", "Romanized": "Dodda", "English": "Big"},
    {"Kannada": "ಚಿಕ್ಕ", "Romanized": "Chikka", "English": "Small"},
    {"Kannada": "ಬೆಲೆ", "Romanized": "Bele", "English": "Price"},
    {"Kannada": "ಸ್ವಲ್ಪ", "Romanized": "Swalpa", "English": "Little"},
    {"Kannada": "ಹೇಗಿದೆ", "Romanized": "Hegide", "English": "How is it"},
    {"Kannada": "ಒಳ್ಳೆದು", "Romanized": "Olledu", "English": "Good"},
    {"Kannada": "ಕೆಟ್ಟದು", "Romanized": "Kettadu", "English": "Bad"},
    {"Kannada": "ಕೆಲಸ", "Romanized": "Kelasa", "English": "Work"},
    {"Kannada": "ವಿದ್ಯೆ", "Romanized": "Vidye", "English": "Education"},
    {"Kannada": "ಉಪಯೋಗ", "Romanized": "Upayoga", "English": "Use"},
    {"Kannada": "ಆಡಳಿತ", "Romanized": "Aadalita", "English": "Management"},
    {"Kannada": "ಆಯುಧ", "Romanized": "Aayudha", "English": "Weapon"},
    {"Kannada": "ಶಕ್ತಿ", "Romanized": "Shakti", "English": "Power"},
    {"Kannada": "ಯುದ್ಧ", "Romanized": "Yuddha", "English": "War"},
    {"Kannada": "ಅಗ್ನಿ", "Romanized": "Agni", "English": "Fire"},
    {"Kannada": "ಜಲ", "Romanized": "Jala", "English": "Water"},
    {"Kannada": "ಧರಿತ್ರಿ", "Romanized": "Dhriti", "English": "Earth"},
    {"Kannada": "ನಕ್ಷತ್ರ", "Romanized": "Nakshatra", "English": "Star"},
    {"Kannada": "ಚಂದ್ರ", "Romanized": "Chandra", "English": "Moon"},
    {"Kannada": "ಸೂರ್ಯ", "Romanized": "Surya", "English": "Sun"},
    {"Kannada": "ಅಜಗಜ", "Romanized": "Ajagaja", "English": "Mountain"},
    {"Kannada": "ಜೀವ", "Romanized": "Jeeva", "English": "Life"},
    {"Kannada": "ಶಾಂತಿ", "Romanized": "Shanti", "English": "Peace"}
]


def quiz_user(words):
    random.shuffle(words)
    score=0
    for word in words:
        print(f"What is the translation of'{word['Kannada']}'/'{word['Romanized']}'? ")
        user_answer=input("Your answer: ").strip().lower()
        correct_answer=word['English'].lower()
        
        if user_answer==correct_answer:
            print("Correct!!\n")
            score+=1
        else:
            print(f"Wrong! The correct answer is '{word['English']}'")
            
    print(f"Quiz Complete! Your Score: {score}/{len(words)}")
    

def main():
    print("Welcome To Language Learning Flashcards Program")
    print("Press ENTER to start the quiz...")
    quiz_user(words)

main()