# IDD_Project

Team Members : Akhil Uddandam, Steve Xue
Big Idea: For our project, we will be developing an fun interactive game using popular computer vision object detection libraries and various hardware devices that we used in the course. The objective of the game is for the players to avoid collision with falling meteorites in order to “survive” the apocalypse. As the player advances through the various difficulty stages, the game will progressively get harder as there will be more objects falling at faster speeds. Only the skilled and alert players will be able to survive the end as we know it!

<img width="433" alt="Screenshot 2022-11-14 at 5 58 52 PM" src="https://user-images.githubusercontent.com/54753807/201785658-7bcc2c23-3d40-4349-a7ec-8057e0c997ea.png">




Parts needed:
We need a computing unit that can do object detection on a video stream. 
A webcam
A monitor that can display the game clearly
Distance Sensors
Smart Bulbs for optional ambience features
Timeline:
We have roughly three weeks in total to complete this project
First week: object detection and figure out how to map a object position into our game
Second week: We will try to implement the game
Third week: We will test it with random users, and make the interaction finer.

Risks/contingencies:

Slow object detection: if the object detection is slow, it will hinder the overall interaction and functionality of the game. 
In game collision: how do we detect in game collision between user figure and meteor.
Multiple object detection: if more than one user comes to play, can the program recognize all of them?

Fall-back plan: 
If the collision detection isn’t working, we can just display the movement of the user on the screen.(meteor hit user, and nothing happens)

If the object detection fails, we will have two distant sensor places at the right end and left end of the playground, and it will keep track of the user’s position.
