from gradio import Interface
from agents import run_nutrition_analysis, run_recipe_generation


def predict(image, mode):
    if mode == 'Nutrition Analysis':
        return run_nutrition_analysis(image)
    return run_recipe_generation(image)

app = Interface(fn=predict, inputs=['image', 'radio'], outputs='text')

if __name__ == '__main__':
    app.launch()
