# debug 연습

a = 23

def find_dog(sound):
    if sound == "멍멍":
        return("개가 짖네")

    else:
        return("다른 동물이구나")

sound = "야옹"
find_result = find_dog(sound)

print(find_result)