import pickle

DEFAULT_RESOLUTIONS = [
    (1920, 1080),
    (1440, 900),
    (1280, 720),
    (1024, 768)
]

def reset_resolutions():
    with open('resolutions.pkl', 'wb') as file:
        pickle.dump(DEFAULT_RESOLUTIONS, file)

if __name__ == "__main__":
    reset_resolutions()
