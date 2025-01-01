
# Project Done by RoboZe ( Prem )

# This Project is the Part of making 5 unique project in 2 days     
# To end the year with the feeling of accomplishment
 


               ### Random fun fact generator ### 




# Step 1: Import necessary libraries
import tkinter as tk
import random

# Step 2: Prepare a list of fun facts
fun_facts = [
    "A day on Venus is longer than a year on Venus. Talk about a long weekend!",
    "Penguins waddle because they're trying to avoid stepping on any landmines. Just kidding, they're just clumsy.",
    "The average person spends two years of their life waiting in line. Enough to make you want to teleport everywhere.",
    "A group of flamingos is called a flamboyance. Sounds like a fancy cocktail party, right?",
    "The longest word in the English language is 'pneumonoultramicroscopicsilicovolcanoconiosis.' Try saying that five times fast!",
    "The first computer bug was an actual bug! Talk about a software glitch with a literal twist.",
    "Polar bears are left-handed. Maybe that's why they're so good at ice fishing—they're ambidextrous!",
    "The average person laughs about 17 times a day. That's enough to keep the world from taking itself too seriously.",
    "There are more than 10,000 different varieties of rice. Enough to make any rice lover's head spin.",
    "The world's smallest mammal is the bumblebee bat. It's so small, it could fit in your teacup (and probably fly away!).",
    "The human brain generates more electrical activity than a city. No wonder we sometimes feel like we're plugged into the Matrix.",
    "A sneeze can travel up to 100 miles per hour. So watch out, bystanders!",
    "The first product to have a bar code was Wrigley's gum. Now that's a sticky situation!",
    "The word 'alphabet' comes from the first two letters of the Greek alphabet: alpha and beta. Simple, yet brilliant!",
    "The longest word in the English language without a vowel is 'rhythms.' A true tongue twister!"
    "The average person blinks about 15-20 times per minute. Wonder how many times they blink during a really boring movie?",
    "The human body sheds about 1.5 million skin cells every hour. That's a lot of dust bunnies!",
    "There are more than 10,000 different types of cheese. Enough to make a cheese lover's dream come true (or a nightmare for lactose-intolerant folks).",
    "The world's largest living organism is a honey fungus in Oregon that covers over 2,200 acres. That's one big fungus amongus!",
    "The first movie to feature a kiss was 'The Kiss' in 1896. Talk about a groundbreaking moment in cinematic history!",
    "The average person eats about 35,000 pieces of candy in their lifetime. No wonder we have cavities!",
    "The word 'goodbye' is a shortened version of 'God be with you.' So the next time you say goodbye, remember you're wishing someone well!",
    "The first electric light bulb was invented in 1879 by Thomas Edison. Talk about a bright idea!",
    "The world's smallest country is Vatican City, which is located within Rome, Italy. Talk about a tiny nation with a big impact!",
    "The average person takes about 2,000 steps per day. Time to get those pedometers moving!",
    "The first Olympic Games were held in 776 BC in Olympia, Greece. That's a long time ago! No wonder they're so competitive.",
    "The world's longest river is the Nile River, which is located in Africa. Talk about a long commute!",
    "The highest mountain in the world is Mount Everest, which is located in Nepal. Climbing it would be a real Everest of a challenge!",
    "The world's largest ocean is the Pacific Ocean. It's so big, you could fit all the continents in it and still have room to spare!",
    "The world's largest desert is the Sahara Desert, which is located in Africa. I wouldn't want to get lost in there!",
    "The world's largest island is Greenland. It's mostly covered in ice, so you might want to pack a parka!",
    "The world's largest country is Russia. That's a lot of land to explore (or get lost in)!",
    "The world's smallest continent is Australia. It's home to kangaroos, koalas, and some seriously cute animals.",
    "The world's largest mammal is the blue whale. It's so big, it could swallow a school bus whole!",
    "The world's fastest land animal is the cheetah. You wouldn't want to have a foot race with one of those guys!",
    "The world's tallest animal is the giraffe. They must have amazing views!",
    "The world's longest living animal is the ocean quahog clam, which can live for over 500 years. Talk about patience!",
    "The world's most venomous snake is the inland taipan. I wouldn't want to mess with that snake!",
    "The world's most poisonous animal is the golden poison frog. It's so poisonous, you could probably use it as a weapon!",
    "The world's largest bird is the ostrich. It's so big, it could probably outrun a horse!",
    "The world's smallest bird is the bee hummingbird. It's so tiny, it could probably fit in your hand (if you were careful enough!).",
    "The world's largest fish is the whale shark. It's a shark, but it's a gentle giant!",
    "The world's smallest fish is the Paedocypris progenetica. It's so small, you'd need a microscope to see it!",
    "The world's largest insect is the Atlas moth. It's so big, it looks like a flying bat!",
    "The world's smallest insect is the fairyfly. It's so small, you could probably fit a million of them on your fingertip!",
    "The world's largest spider is the Goliath birdeater. It's big enough to eat a bird! (Just kidding, probably.)",
    "The world's smallest spider is the Patu digua. It's so small, you could probably fit it on the head of a pin!",
    "The world's largest tree is the General Sherman Tree, a giant sequoia in California, which is over 275 feet tall. That's taller than a 25-story building!",
    "The world's oldest tree is Methuselah, a bristlecone pine in California, which is over 4,800 years old. That's older than most countries!",
    "The world's largest flower is the Rafflesia arnoldii, which can grow up to 3 feet in diameter. It's so big, it looks like something out of a horror movie!",
    "The world's smallest flower is the Wolffia angusta, which is only about 0.5 millimeters long. You'd need a magnifying glass to see it!",
    "The world's largest land animal is the African bush elephant, which can weigh up to 13 tons. That's heavier than most cars!",
    "The world's smallest land animal is the Etruscan shrew, which weighs less than 2 grams. It's so light, you could probably hold it in your hand without even noticing it!",
    "The world's largest reptile is the saltwater crocodile, which can grow up to 23 feet long. That's longer than most cars!",
    "The world's smallest reptile is the Jaragua lizard, which is only about 16 millimeters long. It's so small, you could probably fit it on your fingernail!",
    "The world's largest amphibian is the Chinese giant salamander, which can grow up to 6 feet long. That's bigger than most dogs!",
    "The world's smallest amphibian is the Brazilian froglet, which is only about 9.8 millimeters long. It's so small, you could probably fit it on a dime!",
    "The world's largest mammal on land is the African bush elephant, which can weigh up to 13 tons. That's heavier than most cars!",
    "The world's largest mammal in the sea is the blue whale, which can weigh up to 200 tons. That's heavier than 30 elephants!",
    "The world's fastest land animal is the cheetah, which can run up to 75 miles per hour. You wouldn't want to play tag with one of those guys!",
    "The world's fastest animal in the water is the sailfish, which can swim up to 68 miles per hour. That's faster than most cars!",
    "The world's fastest animal in the air is the peregrine falcon, which can dive at speeds of up to 200 miles per hour. That's faster than a speeding bullet!",
    "The world's longest animal is the bootlace worm, which can grow up to 5"

]
# Step 3: Function to display a random fact
def show_random_fact():
    # Pick a random fact from the list
    random_fact = random.choice(fun_facts)
    # Update the label to show the selected fact
    fact_label.config(text=random_fact)

# Step 4: Set up the GUI application
# Create the main window
root = tk.Tk()
root.title("Random Fun Fact Generator")
root.geometry("600x300")
root.resizable(False, False)

# Add a label to display the fun fact

fact_label = tk.Label(root, text="Click the button to see a fun fact!", wraplength=500, font=("Arial", 14), justify="center")
fact_label.pack(pady=30)

# Add a button to generate a new fun fact

generate_button = tk.Button(root, text="Show Fun Fact", font=("Arial", 12), command=show_random_fact)
generate_button.pack(pady=20)

# Step 5: Run the application

root.mainloop()
