def rate_performance(score):
    if score > 80:
        return "Distinction"
    elif 60 <= score <= 70:
        return "Credit"
    elif 40 <= score <= 50:
        return "Fail"
    else:
        return "Undefined"

# Test the function with some sample scores
scores = [85, 65, 45, 90, 55]
for score in scores:
    print(f"A score of {score} is rated as: {rate_performance(score)}")
    