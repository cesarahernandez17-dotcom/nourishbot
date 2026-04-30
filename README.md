# NourishBot

AI-powered nutrition assistant that analyzes food images and generates nutritional insights or recipe recommendations.

## Overview

NourishBot is a multimodal AI application built to simplify healthy decision-making. Users upload a food image and choose between two workflows:

* **Nutrition Analysis**: estimates calories, macronutrients, and meal quality.
* **Recipe Generation**: detects ingredients and suggests recipes based on dietary preferences.

The project was designed as a practical exploration of AI product development, combining computer vision, LLM workflows, and user-facing interfaces.

## Key Features

* Food image understanding with multimodal AI
* Nutrition estimation (calories, protein, carbs, fats)
* Ingredient detection from meals
* Personalized recipe suggestions
* Dietary filters (vegan, keto, gluten-free, etc.)
* Interactive Gradio interface
* Modular architecture for future scaling

## Tech Stack

* Python
* OpenAI API
* CrewAI
* Gradio
* Pydantic
* LangChain

## Repository Structure

```text
nourishbot/
├── app.py
├── agents.py
├── tools.py
├── schemas.py
├── config.py
├── requirements.txt
├── .env.example
└── notebooks/
```

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

## Run Locally

```bash
python app.py
```

## Product Thinking Behind the Project

This project was built with a product mindset:

* Solves a common user pain point: uncertainty around meals and nutrition
* Combines AI utility with a simple interface
* Supports future monetization through premium plans, meal tracking, and partnerships
* Designed to scale into mobile or B2B wellness use cases

## Future Roadmap

* Meal history and progress tracking
* Barcode scanner
* Personalized goals
* Fitness integrations
* Mobile app version
* Subscription model

## Author

César Hernandez
Product Specialist focused on AI, digital products, and business strategy.

GitHub: GitHub cesarahernandez17-dotcom
