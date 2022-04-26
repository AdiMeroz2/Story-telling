import os
import jsonlines
import openai


# def create_file(name):
#     with jsonlines.open('output.jsonl', 'w') as writer:
#         writer.write_all(name)


def getAnimalName(animal):
    openai.api_key = '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'

    response = openai.Completion.create(
        # model="FINE_TUNED_MODEL",
        engine="text-davinci-002",
        prompt=
        "the name of the animals: "
        "[pig]: [Peppa], [dog]: [Dot], [bear]: [Bell], ["+animal+"]: ",
        temperature=0.4,
        max_tokens=200,
        top_p=0.8,
        frequency_penalty=0,
        presence_penalty=0
    )
    context = response.choices[0].text.split('.')
    context = context[0].split(",")[0]
    context = context.split("[")[1]
    context = context.split("]")[0]
    print(context)
    # print(context[0].split(',')[0])
    # print(context[0])
    # create_file(context)
    return context

def getAnimalSetting(animal):
    openai.api_key = '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'
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=
        "setting of the animals: "
        "pig: was very lazy and never wanted to work, "
        "dog: lived in a house with three family members, "
        "bear: lived in the forest and loves to eat honey, "
        "roaster: was always making too much noise each morning, "
        "whale: lived in the deep ocean"
        +animal+": ",
        temperature=0.4,
        max_tokens=200,
        top_p=0.8,
        frequency_penalty=0,
        presence_penalty=0
    )
    context = response.choices[0].text.split('.')
    context = context[0].split(",")[0]
    contextSplit = context.split()
    if contextSplit[0] == "The":
        context = context.split(' ', 2)[2]
    print(context)
    return context

def fewShot(animal, name, setting):
    openai.api_key = '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'

    response = openai.Completion.create(
        # model="FINE_TUNED_MODEL",
        engine="text-davinci-002",
        prompt=
        "What happened to Betty the bear who loved to eat honey: One day, She finished all the honey in her home "
        "What happened to Richard the roaster who was always making too much noise each morning: One day, all the other animals had enough of him and decided to get rid of him, "
        "What happened to Max the dog who lived in a house with three family members: One day, he saw a stranger attempting to break in to the house, "
        # "What happened to Petter the rabbit: One night, his mother told him a scary story about wolfs, which made him so scared that he couldn't fall asleep, "
        "What happened to Peppa the pig who was very lazy and never wanted to work: One day, she spots an open gate and is out before anyones knows it"
        "What happened to Wilson the whale: One day, he was swimming in the ocean when he suddenly became entangled in a fishing net "
        + "What happened to "+name + " the " + animal + " who "+setting+": ",
        temperature=0.4,
        max_tokens=200,
        top_p=0.5,
        frequency_penalty=0,
        presence_penalty=0
    )
    context = response.choices[0].text.split('.')
    print(context[0])
    return context[0]


def fewShotList():
    openai.api_key = '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'
    output = open('fewShot_output', 'w+')

    with open('animals') as input:
        animals = input.readlines()
        for animal in animals:
            response = openai.Completion.create(
                # model="FINE_TUNED_MODEL",
                engine="text-davinci-002",
                prompt=
                "Betty the Bear: Once upon a time there was a bear called betty. One day, she got lostin the woods and couldn't find her way home, "
                "Richard the Roaster: Once there was a roaster named Richard, he was always making too much noise each morning and pissed the other animals, "
                "Max the Dog: There was a dog named Max. One day, he saw a stranger attempting to break in to the house, "
                "Rabbit: The rabbit fall asleep after some particularly delicious lettuce, and got trapped, "
                "Penguin: The penguin lost it's home and family due to climate change, "
                "Pig: The pig spots an open gate and is out before anyones knows it"
                "Tortoise: Tired of the bragging of a speedy hare, the tortoise challenges it to a race"
                + animal + ": ",
                temperature=0.4,
                max_tokens=200,
                top_p=0.5,
                frequency_penalty=0,
                presence_penalty=0
            )
            context = response.choices[0].text.split('.')
            output.write(context[0])
        # print(context[0])
    return

def zeroShot(name, animal, setting):
    openai.api_key = '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'
    response = openai.Completion.create(
        # model="FINE_TUNED_MODEL",
        engine="text-davinci-002",
        prompt="What happend to "+name+" the "+animal+" who"+setting+": One day, ",
        temperature=0.4,
        max_tokens=200,
        top_p=0.5,
        frequency_penalty=0,
        presence_penalty=0
    )
    context = response.choices[0].text.split('.')
    print(context[0])
    return context[0]

def zeroShotList():
    openai.api_key = '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'
    output = open('zeroshot', 'w+')
    with open('animals') as input:
        animals = input.readlines()
        for animal in animals:
            response = openai.Completion.create(
                # model="FINE_TUNED_MODEL",
                engine="text-davinci-002",
                # prompt="tell a story about a " + animal + ": ",
                prompt="give a story plot about a " + animal + ": ",
                temperature=0.4,
                max_tokens=200,
                top_p=0.5,
                frequency_penalty=0,
                presence_penalty=0
            )
            context = response.choices[0].text.split('.')
            output.write(context[0])
            # print(context[0])
    return

def fineTunes(animal, name, setting):
    openai.api_key = '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'
    # training_file = os.getenv("fine_tuning.jsonl")
    # response = openai.File.create(file=open("fine_tuning.jsonl"), purpose="fine-tune")
    # print(response)
    fineTuneData = open("fineTuning","r")
    # response = openai.FineTune.create(
    #     training_file=training_file,
    #     model="ada",
    # )
    response = openai.Completion.create(
        engine="davinci",
        prompt=fineTuneData.read()+ "/n" +name+" the "+animal + " who "+setting+": One day,",
        temperature=0.4,
        max_tokens=30,
        top_p=0.5,
        frequency_penalty=0.4,
        presence_penalty=0,
        stop=["Q: ",'\n']
    )
    context = response.choices[0].text.split('.')
    print(context[0])
    return

# def fineTunesList(param):


def continueStory(param):
    response = openai.Completion.create(
        # model="FINE_TUNED_MODEL",
        engine="text-davinci-002",
        prompt="continue the story:"+param,
        temperature=0.4,
        max_tokens=800,
        top_p=0.9,
        frequency_penalty=0,
        presence_penalty=0
    )
    context = response.choices[0].text.split('.')
    # print(response)
    print(context)
    return context

def continueStoryList(file):
    openai.api_key = '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'
    output = open('story_list', 'w+')
    with open(file) as input:
        stories = input.readlines()
        for story in stories:
            response = openai.Completion.create(
                # model="FINE_TUNED_MODEL",
                engine="text-davinci-002",
                prompt="tell a long story: " + story ,
                temperature=0.4,
                max_tokens=800,
                top_p=0.9,
                frequency_penalty=0,
                presence_penalty=0
            )
            context = response.choices[0].text.split('.')
            output.write(context[0])
    return

if __name__ == '__main__':
    # create_file("data.json")
    animal = "leopard"
    print("name: ")
    name = getAnimalName(animal)
    print("setting: ")
    setting = getAnimalSetting(animal)
    print("zero shot: ")
    zeroShotStory = zeroShot(name, animal, setting)
    print("few shot: ")
    fewShotStory = fewShot(animal, name, setting)
    print("fine tuning: ")
    fineTunesStory = fineTunes(animal, name, setting)

    # output = open('story_list', 'w+')
    # for story in [zeroShotStory, fewShotStory]:
    #     output.write("Once upon a time there was a "+animal+" named "+name+" who " +setting+". ")
    #     end = continueStory("Once upon a time there was a "+animal+" named "+name+" who " +setting+". "+story)
    #     for line in end:
    #         output.write(line)
    #     output.write("\n")

    # continueStory(zeroPlot)
    # continueStoryList('fewShot_output')
