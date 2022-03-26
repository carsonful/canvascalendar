
# Canvas Assignment Messenger

<img src="https://cdn.discordapp.com/attachments/892918300282077204/957085570142732288/Logo-WhiteonColor.png" data-canonical-src="https://cdn.discordapp.com/attachments/892918300282077204/957085570142732288/Logo-WhiteonColor.png" width="400" height="400" />


> If you'd like to contact me please looked at my [ReadMe](https://github.com/carsonful/carsonful) on how to reach me.

---

### Table of Contents
All sections regarding this repository.

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [License](#license)
- [Author Info](#author-info)

---

## Description

This program allows for users to acquire their To-Do Assignments on Canvas and 
have a message be sent through SMS as well as giving the weather, and a motivational 
quote. This program does not run on it's own. I suggest using a crontab on a VM to 
achieve equivelant output.

For example:


<img src="https://cdn.discordapp.com/attachments/836080339364478986/957088267629654047/IMG_2480.png" data-canonical-src="https://cdn.discordapp.com/attachments/836080339364478986/957088267629654047/IMG_2480.png" width="200" height="400" />



#### APIs

- TextNowAPI 
- CanvasAPI
- OpenWeatherAPI

[Back To The Top](#canvas-assignment-messenger)

---

## How To Use

#### Installation
To be able to execute this code you will need **these** modules:
* PyTextNow
* Datetime
* Time
* CanvasAPI
* Random
* Pandas


#### API Reference

```py
    from canvasapi import Canvas
    from datetime import datetime, timedelta
    import pandas as pd
    import keys

    # Canvas API URL
    API_URL = keys.schoolurl
    # Canvas API key
    API_KEY = keys.accounttoken

    canvas = Canvas(API_URL, API_KEY)
    def getassignments():
        #gets the users todo assignments
        pendingAssigments = canvas.get_todo_items()
        #list with assignment and due date 
        lst = []
        # for loop getting every upcoming assignment
        for assignment in pendingAssigments:

            #gets the name of the assignments
            name = assignment.assignment["name"]

            #gets the time of assignment and subtracts five hours (canvas defaults to GMT I'm EST) - Also assignment is an object 
            # you can call various things from such as ["description"] and etc.
            due = datetime.strptime(assignment.assignment["due_at"], "%Y-%m-%dT%H:%M:%SZ") - timedelta(hours=5)

            #gets the \day of the week
            temp = pd.Timestamp(due)

            #adds the name, time, and day in a list of lists
            lst.append([name, temp.day_name(), str(temp)])

        return lst 
        
```
[Back To The Top](#canvas-assignment-messenger)

---

## References
- [CanvasAPI](https://github.com/ucfopen/canvasapi) Docs
- [PyTextNow](https://github.com/leogomezz4t/PyTextNow_API) Docs
- [OpenWeatherAPI](https://openweathermap.org/guide) Docs


[Back To The Top](#canvas-assignment-messenger)

---

## License

MIT License

Copyright (c) [2022] [Carson Fulmer]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#canvas-assignment-messenger)

---

## Author Info

- LinkedIn - [Carson Fulmer](https://www.linkedin.com/in/carsonfulmer/)
- Website - [Carson Fulmer](http://carsonfulmer.com)

[Back To The Top](#canvas-assignment-messenger)



