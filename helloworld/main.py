import os
import boto3

# Explicit Client Configuration

polly = boto3.client('polly',
                     region_name='eu-west-1',
                     aws_access_key_id=os.getenv('ACCESS_KEY_ID'),
                     aws_secret_access_key=os.getenv('ACCESS_KEY'))

result = polly.synthesize_speech(Text='Hello World!',
                                 OutputFormat='mp3',
                                 VoiceId='Aditi')

# Save the Audio from the resposne
audio = result['AudioStream'].read()
with open('outputs/helloworld.mp3', "wb") as file:
    file.write(audio)
