import random
import pandas as pd

# Define the list of retention strategies
RETENTION_STRATEGIES = [
    "Seasonal Content Updates: Regularly introduce seasonal and thematic content that aligns with holidays and current events to keep the library fresh and engaging.",
    "Mobile Optimization: Ensure the platform's mobile experience is top-notch, with features like downloadable content for offline viewing and mobile-specific user interface enhancements.",
    "Parental Controls: Provide robust parental controls and family-friendly viewing options to appeal to households with children.",
    "Virtual Reality (VR) Experiences: Offer VR content or features that allow viewers to experience movies and TV shows in an immersive environment.",
    "Multi-Language Support: Include multiple language options for content and the user interface to cater to a global audience.",
    "Community Forums: Create a platform-specific community forum where users can discuss their favorite shows, offer recommendations, and connect with other fans.",
    "Collaborative Filtering: Implement a sophisticated collaborative filtering algorithm to improve personalized recommendations based on user interactions across the platform.",
    "Exclusive Screenings: Offer subscribers the chance to attend exclusive online screenings or physical event screenings in various cities.",
    "User-Created Playlists: Allow users to create and share their playlists of shows and movies, which can be featured on the main page to enhance community engagement.",
    "Adaptive Streaming Quality: Automatically adjust streaming quality based on the user's internet speed to ensure smooth playback without buffering.",
    "Reward for Referrals: Introduce a referral program that rewards users with free subscription time or special content access for each new subscriber they bring in.",
    "Enhanced Search Functionality: Develop a highly intuitive search function that allows users to find content based on actors, directors, genres, or even specific quotes or scenes.",
    "Custom Viewing Modes: Offer different viewing modes, such as 'binge mode' with auto-play features or 'cinema mode' with enhanced audio and video settings.",
    "Educational Content Integration: Include documentaries and educational programs that offer learning opportunities for users wanting more than entertainment.",
    "Health and Viewing Analytics: Provide users with analytics on their viewing habits, such as total hours spent watching, most-watched genres, and health reminders to take breaks or adjust brightness and volume for safety."
]

def get_retention_strategies(is_high_paying: bool) -> list:
    """
    Returns a list of retention strategies based on whether the churn user is high paying.
    
    Args:
        is_high_paying (bool): True if the churn user is high paying, otherwise False.
        
    Returns:
        list: Selected retention strategies.
    """
    if is_high_paying:
        # Select 4 random strategies for high-paying churn users
        selected_strategies = random.sample(RETENTION_STRATEGIES, 4)
    else:
        # Select 2 random strategies for other churn users
        selected_strategies = random.sample(RETENTION_STRATEGIES, 2)
    return selected_strategies

def is_user_high_paying(user_payment: float, threshold: float = 50.0) -> bool:
    """
    Determines if a churn user is high paying based on their payment amount.
    
    Args:
        user_payment (float): The amount the user pays.
        threshold (float): The threshold above which a user is considered high paying.
        
    Returns:
        bool: True if the user is high paying, False otherwise.
    """
    return user_payment > threshold

# Example dataset of users (simulate churn users)
data = [
    {"user_id": 1, "payment": 30.0, "churn": True},
    {"user_id": 2, "payment": 80.0, "churn": True},
    {"user_id": 3, "payment": 45.0, "churn": False},
    {"user_id": 4, "payment": 120.0, "churn": True},
    {"user_id": 5, "payment": 25.0, "churn": True}
]

# Create a DataFrame
df = pd.DataFrame(data)

# Filter for churn users
churn_users = df[df['churn'] == True]

# Process each churn user and assign retention strategies dynamically
retention_plan = {}

for _, row in churn_users.iterrows():
    user_id = row['user_id']
    payment = row['payment']
    high_paying = is_user_high_paying(payment)
    strategies = get_retention_strategies(high_paying)
    retention_plan[user_id] = {
        "payment": payment,
        "is_high_paying": high_paying,
        "retention_strategies": strategies
    }

# Output the retention plan for churn users
for user_id, info in retention_plan.items():
    print(f"User {user_id} (Payment: ${info['payment']}, High Paying: {info['is_high_paying']}):")
    for strategy in info["retention_strategies"]:
        print(f"  - {strategy}")
    print()
