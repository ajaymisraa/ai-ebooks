# GPT-4 EBook Generation
Generate a full length e-book in seconds with GPT-4 and GPT-3.5 Turbo! Enter any prompt / book idea of your choosing and an intended audience, and, like magic, a brand new book pdf appears with a custom title! 

## Overall Use Case
Navigate to /backend/main.py and run it after configuring the parameters. Make sure you set your global openai client key up correctly. If this is the route of your choice, then the pdf should be generated after a few seconds in the /backend folder. 

## Web Apps
Probably don't monetize this since it's free reign on github but I added support for Flask and am working on a corresponding frontend that I probably will never finish. It shouldn't be that hard. 

I personally prefer working on backend projects so I might add stuff the the flask support like a rate limiter, LaTeX support (for use cases such as textbooks), and others. This is similar, just a lot less code/math heavy, to my other open-source project, EduGen, which uses GPT-4 and other models to generate practice exams for STEM subjects.
