def calculate_calories_burned(activity, weight_kg, duration_minutes):
    # MET values obtained from https://www.health.harvard.edu/diet-and-weight-loss/calories-burned-in-30-minutes-of-leisure-and-routine-activities
    met_values = {
        'sleeping': 0.9,
        'watching TV': 1,
        'writing, desk work, typing': 1.8,
        'walking, 5.63 kph': 4.3,
        'basketball, shooting baskets': 4.5,
        'bicycling, stationary, 50 watts, light effort': 5.5,
        'running, 8.05 kph (7.5 minute km)': 8,
        'jumping rope': 10,
        'running, 16.09 kph (3.7 min km)': 16
    }

    print(f"Activity received: {activity}")
    print(f"Activity received: {weight_kg}")

    if activity not in met_values:
        return "Invalid activity. Please choose an activity from the list of available activities."

    met = met_values[activity]
    calories_per_minute = met * weight_kg * 3.5 / 200
    calories_burned = round(calories_per_minute * duration_minutes, 2)
    return calories_burned


print(calculate_calories_burned(80, 'sleeping', 30))
