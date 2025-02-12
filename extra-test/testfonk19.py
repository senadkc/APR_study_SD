print("deneme")
def determine_age_group(age):
    if age <= 18:
        return "cocukGenc"
    elif age <= 35:
        return "GencYetiskin"
    else:
        return "Yetiskin"

result = determine_age_group(25)
print("deneme")
print("deneme")