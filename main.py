import winsound
import time
import math
class Sprite:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class EggCodeInterpreter:
    def __init__(self):
        self.variables = {}
        self.sprites = {}
        self.batch_commands = {}

    def play_startup_jingle(self):
        # Define the frequencies for the notes (C, E, G)
        notes = [261.63, 329.63, 392.00]

        # Define the durations for the notes
        durations = [500, 500, 500]

        # Play the notes
        for note, duration in zip(notes, durations):
            winsound.Beep(int(note), duration)
            time.sleep(0.1)  # Add a short delay between notes

    def run(self, code):
        # Play startup jingle
        self.play_startup_jingle()

        lines = code.split('\n')
        for line in lines:
            if line.strip():
                self.execute(line.strip())

        # Keep the interpreter running until exit command is given
        while True:
            user_input = input(">> ")
            if user_input.lower() == "exit":
                print("Exiting EggShell...")
                break
            elif user_input.lower() == "run":
                print("No batch file found. Use 'batch' command to create one.")
            elif user_input.lower().startswith("run "):
                batch_name = user_input[4:].strip()
                if batch_name in self.batch_commands:
                    self.execute_batch(self.batch_commands[batch_name])
                else:
                    print("Batch file not found:", batch_name)
            elif user_input.strip():
                if user_input.lower().startswith("batch"):
                    self.create_batch(user_input[5:])
                else:
                    self.execute(user_input.strip())

    def execute(self, line):
        tokens = line.split()

        if tokens[0] == "set":
            var_name = tokens[1]
            value = tokens[2]
            self.variables[var_name] = value
            print(f"{var_name} set to {value}")

        elif tokens[0] == "print":
            var_name = tokens[1]
            print(self.variables.get(var_name, "Variable not found"))

        elif tokens[0] == "create_sprite":
            sprite_name = tokens[1]
            x = int(tokens[2])
            y = int(tokens[3])
            self.variables[sprite_name] = len(self.sprites)
            self.sprites[sprite_name] = Sprite(x, y)
            print(f"Sprite {sprite_name} created at ({x}, {y})")

        elif tokens[0] == "move_sprite":
            sprite_name = tokens[1]
            dx = int(tokens[2])
            dy = int(tokens[3])
            sprite = self.sprites.get(sprite_name)
            if sprite:
                sprite.move(dx, dy)
                print(f"Sprite {sprite_name} moved by ({dx}, {dy})")
            else:
                print("Sprite not found:", sprite_name)

        elif tokens[0] == "check_collision":
            sprite1_name = tokens[1]
            sprite2_name = tokens[2]
            sprite1 = self.sprites.get(sprite1_name)
            sprite2 = self.sprites.get(sprite2_name)
            if sprite1 and sprite2 and sprite1.x == sprite2.x and sprite1.y == sprite2.y:
                print("Collision detected between", sprite1_name, "and", sprite2_name)
            else:
                print("No collision detected")

        elif tokens[0] == "render":
            self.render()

        elif tokens[0] == "help":
            self.display_help()

        elif tokens[0] == "tips_and_tricks":
            self.display_tips_and_tricks()

        elif tokens[0] == "demo_animation":
            self.demo_animation()

        elif tokens[0] == "draw_line":
            self.draw_line(tokens[1:])

        elif tokens[0] == "draw_rectangle":
            self.draw_rectangle(tokens[1:])

        elif tokens[0] == "draw_circle":
            self.draw_circle(tokens[1:])

        elif tokens[0] == "draw_text":
            self.draw_text(tokens[1:])

        elif tokens[0] == "clear_screen":
            self.clear_screen()

        elif tokens[0] == "play_music":
            self.play_music(tokens[1])

        elif tokens[0] == "stop_music":
            self.stop_music()

        elif tokens[0] == "rotate_sprite":
            self.rotate_sprite(tokens[1:])

        elif tokens[0] == "scale_sprite":
            self.scale_sprite(tokens[1:])

        elif tokens[0] == "flip_sprite":
            self.flip_sprite(tokens[1:])

        elif tokens[0] == "change_sprite_image":
            self.change_sprite_image(tokens[1:])

        elif tokens[0] == "fade_out":
            self.fade_out(tokens[1])

        elif tokens[0] == "fade_in":
            self.fade_in(tokens[1])

        elif tokens[0] == "zoom_in":
            self.zoom_in(tokens[1])

        elif tokens[0] == "zoom_out":
            self.zoom_out(tokens[1])

        elif tokens[0] == "batch":
            self.create_batch(line[6:])

        elif tokens[0] == "calc":
            self.calculate(tokens[1:])

        elif tokens[0] == "//":
            pass  # Ignore comments

        else:
            print("Invalid syntax:", line)

    def execute_batch(self, commands):
        for command in commands:
            self.execute(command)

    def create_batch(self, commands):
        try:
            batch_name, command_str = commands.split(':')
            self.batch_commands[batch_name.strip()] = [command.strip() for command in command_str.split(';')]
            print(f"Batch '{batch_name}' created successfully.")
        except ValueError:
            print("Invalid syntax for batch command. Use 'batch <name>: <commands>'")

    def render(self):
        for sprite_name, sprite in self.sprites.items():
            print(f"Sprite {sprite_name} at ({sprite.x}, {sprite.y})")
        self.display_clock()

    def display_help(self):
        print("EggCode Commands:")
        print("set <variable> <value>: Set the value of a variable")
        print("print <variable>: Print the value of a variable")
        print("create_sprite <sprite_name> <x> <y>: Create a new sprite at the specified position")
        print("move_sprite <sprite_name> <dx> <dy>: Move the sprite by the specified amount")
        print("check_collision <sprite1> <sprite2>: Check if two sprites are colliding")
        print("render: Refreshes screen and displays clock.")
        print("help: Display this help message")
        print("tips_and_tricks: Display tips and tricks for beginners")
        print("demo_animation: Show an animated demo")
        print("draw_line <x1> <y1> <x2> <y2>: Draw a line from (x1, y1) to (x2, y2)")
        print("draw_rectangle <x> <y> <width> <height>: Draw a rectangle at the specified position")
        print("draw_circle <x> <y> <radius>: Draw a circle at the specified position")
        print("draw_text <text> <x> <y>: Draw text at the specified position")
        print("clear_screen: Clear the screen")
        print("play_music <music_file>: Play background music")
        print("stop_music: Stop playing background music")
        print("rotate_sprite <sprite_name> <angle>: Rotate a sprite by the specified angle")
        print("scale_sprite <sprite_name> <scale_factor>: Scale a sprite by the specified factor")
        print("flip_sprite <sprite_name> <direction>: Flip a sprite horizontally or vertically")
        print("change_sprite_image <sprite_name> <image_file>: Change the image of a sprite")
        print("fade_out <duration>: Fade out the screen over the specified duration")
        print("fade_in <duration>: Fade in the screen over the specified duration")
        print("zoom_in <factor>: Zoom in on the screen by the specified factor")
        print("zoom_out <factor>: Zoom out from the screen by the specified factor")
        print("batch <name>: <commands>: Create a batch of commands")
        print("run <batch_name>: Execute the batch of commands")
        print("calc <expression>: Perform a calculation")
        print("exit: Exit EggShell")

    def display_tips_and_tricks(self):
        print("EggCode Tips and Tricks:")
        print("- Use comments (//) to add notes and explanations to your code.")
        print("- Break down your tasks into smaller steps and implement them one by one.")
        print("- Test your code frequently to catch and fix errors early.")
        print("- Don't hesitate to experiment and try out new ideas.")
        print("- Join online communities and forums to get help and learn from others.")
        print("Contact Eli098Git for more info and help.")

    def demo_animation(self):
        # Implement a simple animation demo
        print("Starting demo animation...")
        for i in range(5):
            self.clear_screen()  # Clear the screen before rendering each frame
            self.create_sprite("circle", 10 + i * 2, 5)
            self.render()
            time.sleep(0.5)

    def draw_line(self, params):
        x1, y1, x2, y2 = map(int, params)
        print(f"Drawing line from ({x1}, {y1}) to ({x2}, {y2})")

    def draw_rectangle(self, params):
        x, y, width, height = map(int, params)
        print(f"Drawing rectangle at ({x}, {y}) with width {width} and height {height}")

    def draw_circle(self, params):
        x, y, radius = map(int, params)
        print(f"Drawing circle at ({x}, {y}) with radius {radius}")

    def draw_text(self, params):
        text, x, y = params
        print(f"Drawing text '{text}' at ({x}, {y})")

    def clear_screen(self):
        print("Clearing the screen...")
        self.sprites = {}

    def play_music(self, music_file):
        print(f"Playing music file: {music_file}")

    def stop_music(self):
        print("Stopping music...")

    def rotate_sprite(self, params):
        sprite_name, angle = params
        print(f"Rotating sprite {sprite_name} by {angle} degrees")

    def scale_sprite(self, params):
        sprite_name, scale_factor = params
        print(f"Scaling sprite {sprite_name} by factor {scale_factor}")

    def flip_sprite(self, params):
        sprite_name, direction = params
        print(f"Flipping sprite {sprite_name} {direction}")

    def change_sprite_image(self, params):
        sprite_name, image_file = params
        print(f"Changing image of sprite {sprite_name} to {image_file}")

    def fade_out(self, duration):
        print(f"Fading out over {duration} seconds...")

    def fade_in(self, duration):
        print(f"Fading in over {duration} seconds...")

    def zoom_in(self, factor):
        print(f"Zooming in by factor of {factor}...")

    def zoom_out(self, factor):
        print(f"Zooming out by factor of {factor}...")

    def display_clock(self):
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"Time: {current_time}")

    def calculate(self, expression):
        try:
            result = eval(' '.join(expression))
            print("Result:", result)
        except Exception as e:
            print("Error during calculation:", e)


def display_logo():
    logo = """
     ______
    /      \\
   /        \\
  /__________\\
  \\__________/
   \\        /
    \\______/
    """
    print(logo)

def eggshell():
    interpreter = EggCodeInterpreter()
    code = """
    // Welcome to EggShell
    render
    """
    interpreter.run(code)
    print("\nMade by Eli Hines")
    print("If you bought this product with real money or on a site other than GitHub, you got SCAMMED. Demand your money back.")

if __name__ == "__main__":
    display_logo()
    eggshell()







