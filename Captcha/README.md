
Generate Captcha Using Python

[https://www.geeksforgeeks.org/generate-captcha-using-python/](https://www.geeksforgeeks.org/generate-captcha-using-python/)


In this article, we are going to see how to generate a captcha using Python package captcha to generate our own CAPTCHA (Completely Automated Public Turing Test to Tell Computers and Humans Apart) in picture form. CAPTCHA is a form of challenge-response authentication security mechanism. CAPTCHA prevents automated systems from reading the distorted characters in the picture.



pip install captcha



Generating image captcha: 

    # Import the following modules
    from captcha.image import ImageCaptcha
     
    # Create an image instance of the given size
    image = ImageCaptcha(width = 280, height = 90)
     
    # Image captcha text
    captcha_text = 'GeeksforGeeks' 
     
    # generate the image of the given text
    data = image.generate(captcha_text)  
     
    # write the image on the given file and save it
    image.write(captcha_text, 'CAPTCHA.png')

Generating Audio captcha:

    # Import the following modules
    from captcha.audio import AudioCaptcha
    
    # Create an audio instance
    audio = AudioCaptcha() 
    
    # Audio captcha text
    captcha_text = "5454"
    
    # generate the audio of the given text
    audio_data = audio.generate(captcha_text)
    
    # Give the name of the audio file
    audio_file = "audio"+captcha_text+'.wav'
    
    # Finally write the audio file and save it
    audio.write(captcha_text, audio_file)



















