# Chat-Bot

## Contributors

- Julien CAPOSIENA @julien-cpsn
- Johan PLANCHON @joxcat

## Documentation

- http://doc.aldebaran.com/2-5/naoqi/index.html
- https://gitlab.com/fabricejumel/ihr-raph
- http://doc.aldebaran.com/2-5/naoqi/interaction/dialog/dialog-syntax_full.html?highlight=qichat

## Description

Our Pepper robot do actions based on an alignement matrix. And can converse with the user.

![Main character alignment](images/main_character_alignment.png)

## Ethical Analysis
[Ethical Analysis.xlsx](./Analyse_ethique.xlsx)

## Demo
![demo](./demo.mp4)

## Setup instructions
> You need `python 2.7`, `curl`, `git` or `tar` (to download the repository) and `ssh` 

1. Ssh on the robot using `ssh nao@pepper<N>.local` *(where `<N>` is the pepper number)*
1. Clone the repo in /home/nao/.local/share/PackageManager/apps/chat-bot `git clone https://github.com/Julien-cpsn/chat-bot.git /home/nao/.local/share/PackageManager/apps/chat-bot`
2. Run the code using `env OPENAI_KEY=<openai api key> PYTHONIOENCODING=utf-8 python /home/nao/.local/share/PackageManager/apps/chat-bot/app.py` *(if `python` is bound to `python3` use `python2` in place)*
3. Profit!

## Usage
### On Tablet
> You can see and control the tablet on your computer with the url `http://pepper<N>.local/apps/chat_bot/` *(where `<N>` is the pepper number)*

Clic any of the 9 alignement chart button to choose which action the robot will do. Please refer to the [Story Board](#story-board) for the consequence of the choice.

### With voice
Say the name of any of the 9 alignement chart cases to choose which action the robot will do. Please refer to the [Story Board](#story-board) for the consequence of the choice.

### The assistant
Say "Ok" and then talk to the robot it will transcript the text using Whisper and it will respond using ChatGPT. 

## Story Board

Here is our alignment schema:

<table>
    <tr>
        <td>
            <b>Lawful good</b><br>
            Hug you
        </td>
        <td>
            <b>Neutral good</b><br>
            Hello
        </td>
        <td>
            <b>Chaotic good</b><br>
            SIAMO TUTTI ANTIFASCISTI
        </td>
    </tr>
    <tr>
        <td>
            <b>Lawful neutral</b><br>
            Sumimasen
        </td>
        <td>
            <b>True neutral</b><br>
            Stare at you with no emotions
        </td>
        <td>
            <b>Chaotic neutral</b><br>
            1312
        </td>
    </tr>
    <tr>
        <td>
            <b>Lawful evil</b><br>
            Round with hand
        </td>
        <td>
            <b>Neutral evil</b><br>
            Ping pong break
        </td>
        <td>
            <b>Chaotic evil</b><br>
            Not descriptable
        </td>
    </tr>
</table>

### Lawful good

Comes at you to hug.
![](images/lawful-good.png)

### Neutral good

Say Hello and wave hand
![](images/neutral-good.png)

### Chaotic good

Clap his hands while saying "Siamo tutti antifascisti"
![](./images/chaotic-good.png)

### Lawful neutral

Sumimasen
![](images/lawful-neutral.png)

### True neutral

Stare at your soul with no emotions. Pure void.
![](images/true-neutral.png)

### Chaotic neutral

1312
![](images/chaotic-neutral.png)

### Lawful evil

Round with his hand below the belt.
![](images/lawful-evil.png)

### Neutral evil

A small ping pong break?
![](images/neutral-evil.png)

### Chaotic evil

No description.
![](images/chaotic-evil.png)

