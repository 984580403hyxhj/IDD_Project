Designing Interactive Devices Final Project


Akhil Uddandam 					Steve Xue
au83@cornell.edu							jx288@cornell.edu

12/12/2022


 
Deliverables
1. Project plan: Big idea, timeline, parts needed, fall-back plan.
2. Functioning project: The finished project should be a device, system, interface, etc. that people can interact with.
3. Documentation of design process
4. Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)
5. Video of someone using your project
6. Reflections on process (What have you learned or wish you knew at the start?)
7. Group work distribution questionnaire

IDD Final Project 
Abstract - Our team is creating a thrilling, interactive game using OpenCV libraries and hardware from the course. In this game, players must avoid collisions with falling fireballs to "survive" the apocalypse and save their fellow Cornell Tech students. The game becomes increasingly challenging as more objects fall at faster speeds and players have opportunities to earn points. The players with the highest scores are rewarded with real-world prizes and are featured on leaderboards. Only the most skilled and alert players will be able to survive the end of the world. Are you ready to take on the challenge?

Parts of the game
Raspberry Pi for computing and object detection capabilities, 
Webcam
Monitor for clear game display, 
Distance sensors
Smart bulbs and Speakers for ambiance. 
Button

All of these parts will come together to create an immersive and exciting gaming experience.

Timeline
We have a tight schedule to complete this project, with only three weeks to work on it. In the first week, we will focus on detecting objects and mapping their positions in the game. The second week will be dedicated to implementing the game itself, and in the third week, we will test the game with users and make any necessary improvements. 

Once the project is finished, we plan to present it in class and gather feedback from our peers and professors to make final changes and improvements. Our goal is to create a fully-functional and exciting interactive game that is ready for players to enjoy.

Fall Back Plan
If the collision detection doesn't work as intended, we can still display the movement of the user on the screen, even if the meteor appears to hit them without any consequences. If the object detection fails completely, we can use two distance sensors placed at the right and left ends of the game area to track the user's position. This will allow us to continue the game without relying on object detection.
	


Risk/Contingencies
Slow object detection can negatively impact the overall interaction and functionality of the game. To avoid this, we need to find a way to improve the speed of object detection. 
In order to detect in-game collisions between the user and meteors, we will need to use a combination of object detection and distance sensors to accurately track the positions of both objects. 
If multiple users come to play the game at the same time, we will need to ensure that the program can recognize and track all of them. This may require implementing advanced object detection algorithms that can handle multiple objects simultaneously.

Documentation of design process
The design process for our product follows this general path: 
Brainstorm ideas 
Select a promising idea 
Create sketches of the idea 
Develop the game design and interactions 
Build a prototype 
Test the prototype with users 
Refine the design based on feedback 
Test the refined design to ensure it meets the desired goals and user needs. This process allows us to iteratively improve the design of our product and ensure that it meets the needs and expectations of users.

Ideation:
To start, we had a discussion about potential project ideas that involved using OpenCV, as we were both interested in learning more about it. We brainstormed a range of concepts, including games, posture recognition devices, and AI-powered personal trainers. Some specific ideas we came up with included a racing game that uses hand recognition, a Snake game with OpenCV, and image classifiers to monitor weight lifting form using TensorFlow.

Pick a Idea:
After considering our options, we decided to create a game that is inspired by the classic arcade game Space Invaders. We wanted to make the game more interactive, so we added body movement as a way to control the game, in addition to buttons. In the game, players must dodge fireballs by moving their bodies, and their movements will be detected using OpenCV's human body detection feature. The player's position in the game will be determined based on their body movements, and they will be rewarded for successfully dodging fireballs and saving people. Are you ready to take on the challenge?


Sketches:
In the game, the player must dodge fireballs in order to score points and continue playing. If they fail to dodge the fireballs, the game will end and the player will lose. The objective is to earn as many points as possible by successfully dodging fireballs and saving people. The game becomes increasingly challenging as the player progresses, with more fireballs falling at faster speeds. Only the most skilled and alert players will be able to survive and earn high scores. 

Game Design:
Motivation: To add an extra layer of challenge and engage players, we've introduced human figures that players can save by touching them in the game. This adds an additional goal for players to strive for and makes the game more exciting. In addition to dodging fireballs, players must also save people to earn points and advance in the game. This adds a new level of complexity to the game, making it more interesting and motivating for players.

Core Objective: The main objective of the game is for players to earn as many points as possible by avoiding obstacles and saving people. The game will last for 8 minutes, during which players can earn points by avoiding fireballs and saving people. Additionally, players will have the opportunity to earn even more points through various perks and bonuses that can be activated with the click of a button (when “unlocked”). The ultimate goal is to earn as many points as possible within the time limit.

Interaction Design:
In addition to designing the game, we also created different interactions to encourage players to engage with it in the way that we anticipated. They are described below.

Sound: When a player hits a fireball, we added an "ouch" sound to indicate that they did something wrong and to punish them. When they save the player, we play a "thank you" sound to reward them for doing it correctly.

Perks/Rewards: To reward players for their progress in the game, we've implemented a system that grants bonuses when players reach certain point thresholds. For example, when a player reaches 25 points, they are rewarded with 30 seconds of invisibility, during which they will not lose points for colliding with fireballs. Similarly, when a player reaches 50 points, they are rewarded with 30 seconds of double points, allowing them to earn even more points. These bonuses help keep the game interesting and motivate players to continue playing.

Button: To activate the above perks, the user must press the button.

Distance Sensor: To ensure accurate object detection, we've implemented a system that uses distance sensors to keep players within the optimal "game zone" for object detection. If a player moves outside of this zone, the game will issue a warning through the speakers, instructing the player to reposition themselves. This helps prevent errors in object detection and ensures a smooth and enjoyable gameplay experience.

Prototype and User Testing:
We built a prototype of the game and tested it on our classmates and roommates during a showcase. The feedback we received was mostly positive, but there were a few suggestions for improvement. Some people thought the shape of the fireball was ambiguous and that it was unclear whether players should touch it or avoid it. Others suggested that the game could benefit from more hardware interactions. We are considering these suggestions as we continue to develop the game.

We also find out the hardware limitations of the device that human body detection is very unstable, the model often mistaken other objects as human body, or simply just didn’t recognize human body. Human body also takes a lot of computation power that the device can’t run it smoothly. Thus we change the human body detection to hand detection, where it is faster and more accurate.

Refine:
We took the feedback we received during the showcase and used it to refine our prototype. We changed the shape of the fireball to a meteor with a fiery tail, and added visual feedback in the form of a blood stain on the screen when players touch it. This helps players understand that they have been hit and encourages them to avoid the fireballs in the future. Additionally, we added an in-game feature that allows players to press a physical button to turn all fireballs into donuts for a short period of time when they earn enough points. This encourages players to continue playing and rewards them for their progress, while also making the device more interactive. Overall, these changes have improved the gameplay experience and made the game more enjoyable for players.

Archive of all code, design patterns, etc. used in the final design.
All of the code for our project can be found on GitHub at the following link: https://github.com/984580403hyxhj/IDD_Project 
Following screenshots are code examples from the github, they include project setup, hand recognition, collision detection, etc. Details are in github. Also the sprites and artworks used are also in the github folder as well.

 
Please feel free to check out our code and use it as a reference for your own projects. If you have any questions or feedback, please don't hesitate to reach out to us. We would be happy to help.
Video Demo
In the following video, we demonstrate the game in action. We showcase the gameplay, the interactive devices used, and the features of the game.
https://youtu.be/VFo6i9PBtJ8
 
Reflections on process
In this project, we designed and built an interactive game using OpenCV libraries and hardware from the Interactive Device Design course. Our goal was to create an exciting and engaging experience for players, and we were able to achieve this by implementing a game in which players must avoid collisions with falling fireballs to "survive" the apocalypse and save their fellow Cornell Tech students. 
One of the biggest challenges we faced was implementing object detection and collision detection in the game. We spent a significant amount of time working on this aspect of the project, and we were able to improve the speed and accuracy of object detection by using a combination of algorithms and hardware. Additionally, we added features and bonuses to make the game more interesting and engaging, such as the ability to turn all fireballs into donuts when players earn enough points. 
Overall, we learned a lot from this project and gained valuable experience working with OpenCV and hardware. We are proud of the final product and believe it is a fun and exciting game that players will enjoy. In the future, we would like to continue improving the game and exploring new possibilities for interactive devices.
Work Distribution
For this project, Akhil contributed significantly to the ideation and development phases, while Steve focused on the technical aspects of implementation. Both of us contributed creatively and had a great time brainstorming ideas and bringing the project to life. We had a lot of fun working on this project and learned a lot about interactive devices. Overall, it was a great collaborative experience and we are proud of the final product.
