# Real Madrid All-Stars

---

![img.png](github/img.png)
Hola amigo, this project aims to provide information about the best players played for the club in the history of football.

- All the information is double-checked and stored manually. It's not just a reshape of a Kaggle database, but handpicked and sorted fine data.

![img.png](github/img23.png)
Information was taken from:
- RealMadrid.com
- Transfermarkt.com


All data is kept in json format: Example:

```json
{
  "Defender": [
    {
      "name": "Cannavaro",
      "full_name": "Fabio Cannavaro",
      "country_id": "2",
      "position": "Defender",
      "number": [
        "5"
      ],
      "appearances": "106",
      "goals": "1"
    }
  ],
  "Midfielder": [
    {
      "name": "Beckham",
      "full_name": "David Robert Joseph Beckham",
      "country_id": "9",
      "position": "Midfielder",
      "number": [
        "23"
      ],
      "appearances": "159",
      "goals": "20"
    }
  ]
}
```
The files [real_madrid.json](real_madrid.json) and [countries.json](countries.json) the most important ones.
Btw they will be updated by the time. However, if you want to participate in the project by adding legends only.

This project has no licence.

[![Watch the video](https://i.ytimg.com/vi/rtYDRwfPXKM/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCBIX_AdFbSeyH8Fi6vQ6F78oDtwg)](https://youtu.be/Yc-7IQqcqeM?si=MufgRRxBI-yEOEc1)

---

## Benefits of the database

- If you care about the numbers the players wore.
- Precise data, as I check every single player by myself, all data is 100% correct. For example - Emilio Butragueno, a lot of datasets don't count his friendly games as appearances, just because that is scrapped from Google/elsewhere low-quality data. Here, I manually count and update a lot of details for the best information. 
- If you want to generate reports on the best players only. 

---
## Contribution

Feel free to contribute. Run thr `main.py` file, put your input, whenever you are done, you can push changes. 
As it's an open source repo and will always be you will always have access to `real_madrid.json` file. 

Later on you can create your games, APIs based on that json file.


---
![img_1.png](github/img_1.png)
Vamos Real, Hala Madrid
