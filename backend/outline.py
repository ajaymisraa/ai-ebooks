# Generate text of an ebook w/ GPT-4 API, then with that, return the text to main.py.

from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def cover(topic, audience):
    response = client.images.generate(
        model="dall-e-3",
        prompt="Generate an cover image for a book about " + topic + " for the audience " + audience + ". This image does not intend to be a pictue of a book, rather, it should be a general image on the topic with the tone set for the audience of" + audience + ".",
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    print("Cover generated")
    return image_url

def outline(topic, audience, chaptercount, sectioncount):
    response = client.chat.completions.create(
        model="gpt-4",  # Replace with the specific GPT-4 model identifier
        messages=[
            {"role": "system", "content": "You are a helpful publisher. You write outlines for ebooks. All of your outputs should be in json format. If an error were to arise anywhere ever, please JUST return '404'."},
            {"role": "user", "content": 
             f"Create a detailed ebook outline for a book on the topic '{topic}' targeted towards '{audience}'. Include a title, chapters, and subsections. Have the json format be like this: {'{'}'title': 'title', 'name of chapter 1': ['chapter1section1', 'chapter1section2', 'chapter1section3'], 'name of chapter 2': ['chapter2section1', 'chapter2section2', chapter2section3]{'}'}, etc etc. There should be {chaptercount} chapters and {sectioncount} sections per chapter."
             f"Ensure that the outline is in this format. For chapter names, do 'Chapter #: Chapter Title', for section names, name each of them '(Chapter Number).(Section Number) (Section Name)",
             }
        ]
    )

    if response.choices[0].message.content == "404":
        print ("Error in outline generation")
        return "404"

    print("Outline generated.")
    return response.choices[0].message.content

def content(topic, audience, bookoutline):
    ebook_outline = json.loads(bookoutline)

    for chapter, subsections in ebook_outline.items():
        if chapter == "title":
            continue
        ebook_outline[chapter] = {sub: [] for sub in subsections}  

    def generate_content_for_subsection(subsection):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content": "You are a helpful publisher. You write content for ebooks. If an error were to arise anywhere ever, return the error."},
                {"role": "user", "content":
                    f"Write a detailed, informative and engaging content about '{subsection}'. The content should be approximately 10 paragraphs long. The topic for this ebook is {topic} and the intended audience is {audience}. Ensure that you return just the pargraphs. Don't return anything else. Do not return any headers, titles, names, or anything. Just return the paragraphs. DO NOT INCLUDE NUMBERS. Like do not put 'Paragraph 1:' or anything. Just return the paragraphs' data.",
                }
            ]
        )
        paragraphs = [para.strip() for para in response.choices[0].message.content.strip().split('\n') if para.strip()]
        return paragraphs

    # Generating content for each subsection
    for chapter, subsections in ebook_outline.items():
        if chapter == "title":
            continue
        for subsection in subsections:
            content = generate_content_for_subsection(subsection)
            ebook_outline[chapter][subsection] = [{"paragraph": para} for para in content]  # Appending content as paragraphs

    # Convert to JSON
    print("Contents generated.")
    return json.dumps(ebook_outline, indent=4)
