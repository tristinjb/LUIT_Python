#!usr/bin/envpython3.7

#Python Packages
# creating a reqiurement.text so the code created or shared and be use and shared in other environments
# ~pip freeze > requirements.txt~


#Funtion labs

#lab 1- A simple function
# A function that prints hello world
def hello_world():
    print('hello world')

# A function that returns hello world
def hello_world():
    return 'hello world'

# Assign the hello_world() function to a variable.
greeting = hello_world()
print(greeting)


#lab 2- Introduction to boto3
import boto3

client = boto3.client('translate')

def translate_text(): # declare the function using def, name, braces for parameters and a colon  
    response = client.translate_text(
        Text='I am learning to code in AWS', # Assigning the value of the string to the variable Text
        SourceLanguageCode='en', # We are using a two letter language code from the documentation (en = English)
        TargetLanguageCode='fr' # We use a second two letter language code from the documentation (fr = French)
    )
    
    print(response) # this code is inside the function and will print the contents of the variable 'response' 

translate_text() # This line will call our function. Without it, python will not do anything.


#lab 3- The main() function
import boto3

client = boto3.client('translate')

def translate_text():
    response = client.translate_text(
        Text='I am learning to code in AWS',
        SourceLanguageCode='en',
        TargetLanguageCode='fr'
    )
    print(response) # this code is inside the function and will print the contents of the variable 'response'

def main():
    translate_text()

if __name__=="__main__":
    main()
 
    
#Arguments and Parameters

#lab 4- Argumemts
#step 1- Postional argumnets

import boto3

def translate_text():
    client = boto3.client('translate')
    response = client.translate_text(
        Text='I am learning to code in AWS', 
        SourceLanguageCode=source_language_code, 
        TargetLanguageCode=target_language_code 
    )
    print(response) 

def main():
    translate_text('I am learning to code in AWS','en','fr')

if __name__=="__main__":
    main()

#step 2- Keyword Arguments

import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 
kwargs={
    "Text":"I am learning to code in AWS",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"fr"
    }
def main():
    translate_text(**kwargs)

if __name__=="__main__":
    main()