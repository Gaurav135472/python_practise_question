def greet(fx):
    def mfx():
        print("Good morning")
        fx()
        print("Hows going ?")
    return mfx

@greet
def hello():
    print("Hello world")
    
hello()