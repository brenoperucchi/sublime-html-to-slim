HTML2Slim now includes customizable settings, allowing you to tailor the environment to your specific development needs

Navigate to Preferences -> Package Settings -> HTML2Slim -> Settings User

- "default_user_path": "/Users/your_username/" - This sets the base path for your user environment.
- "default_rails_path": "/Users/your_username/your_railsproject" - This specifies the path to your Rails project directory.

### Requirements:
- HTML2Slim version 0.2.3 - https://github.com/brenoperucchi/html2slim
- RBENV for managing Ruby environments.

Please Let me know if you have any issues.

Clone the repository in your Sublime Text "Packages" directory:
* OS X:

    ```bash
    cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages
    git clone https://github.com/brenoperucchi/html2slim.git "HTML2Slim"
    ```

Original Content:

--------------------------------------------------------------------------------------------------------------------------
# HTML to Slim plugin for Sublime Text 3

Converts files, selection and clipboard content from HTML or ERB to Slim using the [htm2slim gem](https://github.com/slim-template/html2slim).

Most of this code base and this readme is from the [html-to-haml project](https://github.com/pavelpachkovskij/sublime-html-to-haml)

## Installation

### [Sublime Package Control](http://wbond.net/sublime_packages/package_control)

In the command Pallette choose **Package Control: Install Repository** and select **HTML2Slim**

### Git installation

Clone the repository in your Sublime Text "Packages" directory:

    git clone git@github.com:JohnAgan/sublime-html-to-slim.git "HTML2Slim"

The "Packages" directory is located at:

* OS X:

        ~/Library/Application Support/Sublime Text 3/Packages/

* Linux:

        ~/.config/sublime-text-3/Packages/

* Windows:

        %APPDATA%/Sublime Text 3/Packages/

## Usage

* **Convert hole ERB or HTML file** `Shift+Alt+F` - creates new file in the same folder using the same name as the source ending with '.html.haml'.
* **Convert selection** `Shift+Alt+S` - replaces selection of HTML or ERB with Slim content.
* **Convert clipboard content** `Shift+Alt+V` - inserts Slim of converted clipboard HTML or ERB content.

### In Command Palette:

* **HTML2Slim: Convert file**
* **HTML2Slim: Convert selection**
* **HTML2Slim: Convert clipboard content**