import time
import random
import logging
from dataclasses import dataclass
from typing import List

# Configure logging to visualize the "bot's" thinking process
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [BOT_ENGINE] - %(message)s',
    datefmt='%H:%M:%S'
)

@dataclass
class UserProfile:
    username: str
    is_private: bool
    follower_count: int

class MockInstagramAPI:
    """
    Simulates the Instagram API for research purposes.
    Does NOT make real network requests.
    """
    def __init__(self):
        self.rate_limit_counter = 0
        self.start_time = time.time()
        logging.info("Connected to Mock Instagram Network (Simulation Mode)")

    def get_user_profile(self, username: str) -> UserProfile:
        # Simulate network latency
        time.sleep(random.uniform(0.1, 0.4)) 
        return UserProfile(username=username, is_private=False, follower_count=random.randint(100, 5000))

    def follow_user(self, target_username: str) -> bool:
        """Simulates sending a follow request"""
        # Simulate network packet round-trip time
        latency = random.uniform(0.3, 0.8)
        time.sleep(latency)
        
        # Simple simulation of platform-side rate limiting detection
        self.rate_limit_counter += 1
        return True

class BotBehaviorModel:
    """
    Implements human-mimicry logic for studying automation behavior.
    """
    def __init__(self, target_page: str):
        self.api = MockInstagramAPI()
        self.target_page = target_page
        self.actions_performed = 0
        
        # BEHAVIORAL PARAMETERS (For Research)
        self.mean_delay = 3.0      # Average seconds between actions
        self.jitter = 1.5          # Random variance (+/-)
        self.break_probability = 0.2 # 20% chance to take a long break

    def calculate_human_delay(self) -> float:
        """
        Generates a delay that follows a Gaussian-like distribution 
        to mimic organic human interaction speeds.
        """
        base = random.gauss(self.mean_delay, self.jitter)
        return max(0.5, abs(base)) # Ensure delay is never negative or instant

    def run_simulation(self, goal_followers: int):
        logging.info(f"Starting simulation for target: {self.target_page}")
        logging.info(f"Goal: Increase by {goal_followers} (simulated)")

        # Target list (Simulated potential followers)
        potential_targets = [f"user_{i}" for i in range(101, 101 + goal_followers)]

        for target in potential_targets:
            logging.info(f"--- Processing Target: {target} ---")
            
            # 1. Human Emulation: Navigation
            logging.info("Emulating: Navigating to user profile...")
            profile = self.api.get_user_profile(target)
            
            # 2. Logic: Decision making
            if profile.is_private:
                logging.warning(f"Skipping {target} (Private Profile)")
                continue

            # 3. Human Emulation: "Thinking" time / Jitter
            delay = self.calculate_human_delay()
            logging.info(f"Behavior: Waiting {delay:.2f}s to mimic reading bio...")
            time.sleep(delay)

            # 4. Action: Interact
            logging.info(f"Action: Clicking 'Follow' on {target}")
            success = self.api.follow_user(target)

            if success:
                self.actions_performed += 1
                logging.info(f"Success: Now following {target}")
            
            # 5. Randomized Breaks (Anti-Detection Pattern)
            if random.random() < self.break_probability:
                short_break = random.uniform(5.0, 10.0)
                logging.info(f"Pattern: Taking a short break ({short_break:.2f}s) to look organic...")
                time.sleep(short_break)

        logging.info("--- Simulation Complete ---")
        logging.info(f"Total simulated actions: {self.actions_performed}")
        logging.info("Note: No real API requests were made.")

if __name__ == "__main__":
    # Example Usage
    bot = BotBehaviorModel(target_page="athar_sleeve")
    bot.run_simulation(goal_followers=5)
