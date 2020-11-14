
# create a BMI cal using OOP
class BMI:
    # below expects weight and height
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.pi = 3.14   # constant
        # above we define attr/var


    def get_bmi(self):
        answer = self.weight/(self.height ** 2)
        print('Your Body_Mass is ', answer)


w = float(input('What is your Weight'))
h = float(input('What is your Height'))
object  = BMI(w, h)
object.get_bmi()

# Option 1
# Google Colab Cloud  - Jupyter Notebook
# Watson Studio Cloud  - Jupyter

# Option 2
# in your laptop install Jupyter Notebook
# from jupyter.net




