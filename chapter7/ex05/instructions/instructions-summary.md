# Scenario
Suppose you work for an electronics company that has a new MoviePlayer device that it wants to release to the market. The software for this device needs to support over-the-air updates that enables users to watch their favorite movies painlessly. 

# Aim
Create a class that represents a portable movie player, `MoviePlayer`. The `MoviePlayer` class should have a `play` method, which sets the first movie from the list of movies as currently playing. The list of movies should be a `private` attribute. Additionally, it should have a firmware version attribute and an update firmware class method that updates the firmware version.

# Steps for Completion

1. Go to your *main.py* file.

2. Define the `MoviePlayer` class by adding the `firmware_version` class attribute and assigning it a value of **1.0**.

3. Define the initializer method `__init__` and pre-populate the movie list with a few movies. Make sure the movies store is `private`.

4. Define the `play` method, which sets the `current_movie` attribute to the first item in the movies list.

5. Define the `list_movies` method, which returns the list of movies in the `MoviePlayer`.

6. We'll add the `update_firmware` version method, which checks for whether the new version being provided is more recent than the current firmware version before updating.

7. We then add a few test lines to the `main` method and run the script as shown in *Snippet 7.67*:
```python
    player = MoviePlayer()
    print("Movies currently on device:", player.list_movies())

    player.update_firmware(2.0)
    print("Updated player firmware version to", player.firmware_version)

    player.play()
    print("Currently playing", f"'{player.current_movie}'")
```
<sup>*Snippet 7.67*</sup>

We can run the script by entering *python3 main.py* in the terminal. The output should look similar to *Figure 7.6*:

![PF1e-7-5-figure-7.6.png](../assets/unCnMbK8QpGBzfagxLgo.png)

<sup>*Figure 7.6*</sup>