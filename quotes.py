"""
╓═════════════════════════════════════════════════☆═════════════════════════════════════════════════╖
    
    quotes.py Provides a random quote using the random module which allows for me to call for a 
    random quote inside the list. Planning on updating so maybe it could scrape a website possibly?
                                                                                                    
╙═════════════════════════════════════════════════☆═════════════════════════════════════════════════╜
"""



import random

motivation = [
"“Try not to become a man of success but rather become a man of value.” – Albert Einstein",
"“A winner is a dreamer who never gives up.” – Nelson Mandela",
"“If you don’t have a competitive advantage don’t compete.” – Jack Welch",
"“The only thing standing in the way between you and your goal is the BS story you keep telling yourself as to why you can’t achieve it.” – Jordan Belfort",
"“What is life without a little risk?” – J.K. Rowling",
"“Only do what your heart tells you.” – Princess Diana",
"“If it’s a good idea go ahead and do it. It’s much easier to apologize than it is to get permission.” – Grace Hopper",
"“I attribute my success to this: I never gave or took an excuse.” – Florence Nightingale",
"“The question isn’t who is going to let me; it’s who is going to stop me.” – Ayn Rand",
"“A surplus of effort could overcome a deficit of confidence.” – Sonia Sotomayer",
"Motivational Quotes from Books",
"“And when you want something all the universe conspires in helping you to achieve it.” ― Paulo Coelho The Alchemist",
"“Your playing small does not serve the world. There is nothing enlightened about shrinking so that other people won’t feel insecure around you. We are all meant to shine as children do.” – Marianne Williamson A Return to Love: Reflections on the Principles of “A Course in Miracles”",
"“Don’t think or judge just listen.”― Sarah Dessen Just Listen",
"“I can be changed by what happens to me. But I refuse to be reduced by it.” – Maya Angelou Letter to My Daughter",
"“Darkness cannot drive out darkness: only light can do that. Hate cannot drive out hate: only love can do that.” ― Martin Luther King Jr. A Testament of Hope: The Essential Writings and Speeches",
"“You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. You’re on your own. And you know what you know. And YOU are the one who’ll decide where to go…” ― Dr. Seuss Oh the Places You’ll Go!",
"“It’s the possibility of having a dream come true that makes life interesting.” ― Paulo Coelho The Alchemist",
"“There is some good in this world and it’s worth fighting for.” – J.R.R. Tolkien The Two Towers",
"“Learn to light a candle in the darkest moments of someone’s life. Be the light that helps others see; it is what gives life its deepest significance.”― Roy T. Bennett The Light in the Heart",
"“Atticus he was real nice.” “Most people are Scout when you finally see them.” ― Harper Lee To Kill a Mockingbird",
"Motivational Quotes from Movies",
"“Oh yes the past can hurt. But the way I see it you can either run from it or learn from it.” – The Lion King",
"“We’re on the brink of adventure children. Don’t spoil it with questions.” – Mary Poppins",
"“Life moves pretty fast. If you don’t stop and look around once in a while you could miss it.”– Ferris Bueller",
"“I just wanna let them know that they didn’t break me.” – Pretty in Pink",
"“I’m going to make him an offer he can’t refuse.” – The Godfather",
"“No one has ever made a difference by being like everyone else.” – The Greatest Showman",
"“Spend a little more time trying to make something of yourself and a little less time trying to impress people.” – The Breakfast Club",
"“The problem is not the problem. The problem is your attitude about the problem.” – Pirates of the Caribbean",
"“Remember you’re the one who can fill the world with sunshine.” – Snow White",
"“You’ll have bad times but it’ll always wake you up to the good stuff you weren’t paying attention to.” – Good Will Hunting"
]


def getrandomquote():
    x = random.choice(motivation)
    return x 

