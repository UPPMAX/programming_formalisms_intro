# Setup
<base target="_blank">

Parts taken from [https://nbis-reproducible-research.readthedocs.io/en/course_2104/setup/](https://nbis-reproducible-research.readthedocs.io/en/course_2104/setup/)
 and [https://coderefinery.github.io/installation/](https://coderefinery.github.io/installation/)

**There are several solutions in how to work with coding and the environments around it**
- You can work in the environment(s) you are used to.
- Many of the teachers will use **Visual Studio Code (VS code)**
- This is not necessary if you have other solution
- Benefit:  
  - integrate you terminal and Git work with **code development**
  - graphical user interface
  - available in **all platforms**
 
- [Install VS Code](https://code.visualstudio.com/)

- Follow the steps from [configure git](https://uppmax.github.io/programming_formalisms_intro/setup.html#configure-git) if not done already
- Follow the steps from [configure GitHub](https://uppmax.github.io/programming_formalisms_intro/setup.html#github) if not done already
- Follow the steps from [configure ssh-keys](https://uppmax.github.io/programming_formalisms_intro/setup.html#git-github-connection-through-ssh-keys-this-may-take-a-while-to-get-working-but-is-worth-it) if not done already

## Shell and Git
If you will not use VS code, follow steps below.
 
### Terminal & git

**Git and terminals are already integrated in VS Code and can be the first choice**
Otherwise follow the steps below!

`````{tabs} 
````{tab} Mac & Linux

- We will use terminal to some extent.
- Choose one of your choice, the built-in or another!

- Chances are big that you already have **git installed on your computer**. You can check by running e.g. `git --version`. 
- If you don't have git, install it following the instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) 
- If you have a very old version of git you might want to update to a later version.
````

````{tab}  Windows

There are several different ways to run the course material on a Windows computer. Neither is perhaps optimal, and the material itself has not been adapted specifically for Windows. Nevertheless, in principle everything *should* be possible to run. A few ways you could setup:

**Git-windos with a command line and Git integrated**

- Install Git Windows: [https://gitforwindows.org/](https://gitforwindows.org/?to=/placeholder.com) (**easiest if you want to start fast and plan to work in windows environment**)
      
   - See Windows part at [https://coderefinery.github.io/installation/shell-and-git/#installation](https://coderefinery.github.io/installation/shell-and-git/#installation)
   - Included will be the **Git Bash**

**Other possibilities**
- Use the **Windows 10 PowerShell**

  - [install git](https://git-scm.com/book/en/v2/Appendix-A%3A-Git-in-Other-Environments-Git-in-PowerShell)
        
- Use the Linux Bash Shell (**WSL**) on Windows 10/11 (**perhaps best practice if you plan to run Linux as well**)
   - This will give you access to a full command-line bash shell based on Linux on your Windows 10/11 PC. 
   - instructions below
   - For the difference between the Linux Bash Shell and the PowerShell on Windows 10, see *e.g.* [this article](https://searchitoperations.techtarget.com/tip/On-Windows-PowerShell-vs-Bash-comparison-gets-interesting).

- Run as Linux through a **virtual machine** (and see the Linux setup above)
  - not shown

**Install Bash on Windows 10/11 (WSL)**, following the instructions at *e.g.* **1** of these resources:


- [Installing the Windows Subsystem and the Linux Bash](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
- [Installing and using Linux Bash on Windows](https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/)
- [Installing Linux Bash on Windows](https://itsfoss.com/install-bash-on-windows/)
````
`````

### Configure git

**This must be done**

Follow these instructions. [https://nbis-reproducible-research.readthedocs.io/en/course_2104/setup/#installing-git](https://nbis-reproducible-research.readthedocs.io/en/course_2104/setup/#installing-git)

### GitHub
Sign up for GitHub account:
[https://coderefinery.github.io/installation/github/](https://coderefinery.github.io/installation/github/)

### Git/GitHub connection through ssh keys 
(This may take a while to get working, but is worth it)
[https://coderefinery.github.io/installation/ssh/](https://coderefinery.github.io/installation/ssh/)

- Test: `ssh -T git@github.com`
  - Output should be something like this: ``Hi bclaremar! You've successfully authenticated, but GitHub does not provide shell access.`` 
- If not working, these are the approximate steps to be done in your terminal. It can vary between systems, so link above is more certain.

```console
$ ssh-keygen -t ed25519 -C "<email address for your GitHub account>"
$ eval "$(ssh-agent -s)"
$ ssh-add ~/.ssh/id_ed25519
$ # Copy the SSH public key to your clipboard.
$ clip < ~/.ssh/id_ed25519.pub
```

- Then go to your GitHub account on the web.
  1. In the upper-right corner of any page, click your profile photo, then click Settings.
  2. In the "Access" section of the sidebar, click SSH and GPG keys.
  3. Click New SSH key or Add SSH key.
  4. In the "Title" field, add a descriptive label for the new key. For example, if you're using a personal laptop, you might call this key "Personal laptop".
  5. Select the type of key **authentication**.
  6. In the "Key" field, paste your public key.
  7. Click Add SSH key.
  8. If prompted, confirm access to your account on GitHub.

- Now test again in your terminal: `ssh -T git@github.com`
  - Output should be something like this: ``Hi bclaremar! You've successfully authenticated, but GitHub does not provide shell access.`` 

- If there was a problem, confer the full article [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).
  -   


## Python
- Use what you already have
- If you don't have Python there are different ways to go. We won't use Conda during the lessons, for instance.
  - Bare python (recommended for the **"bare metal" user**)
    - you need to install other packages (pip)
    - [install python](https://www.python.org/downloads/)
    - **note macOS**: the system install of Python on macOS is not supported, instead:
      - ``brew install python3`` 
  - Anaconda (recommended for **python/R developers liking GUI:s**)
    - includes many many packages
    - includes conda packager
    - GUI launchers, like example
    - jupyter notebook/lab
    - Spyder
    - RStudio
    - etc...
    - [install Anaconda](https://www.anaconda.com/download)
  - miniconda (recommended for **terminal user**)
    - less packages than Anaconda, and no GUI launcher but:
    - conda packager
    - pip
    - etc...
    - [install Miniconda](https://docs.conda.io/projects/miniconda/en/latest/)

- In Linux and Bash, Python should work from the command line by typing ``python``/``python3`` or running a script with ``python <script>``/``python3 <script>``

### In VS Code

- Step 1. Install a supported version of Python on your system 
  - note: that the system install of Python on macOS is not supported
  - ``brew install python3`` 
- Step 2. Install the Python extension for Visual Studio Code.
- Step 3. Open or create a Python file and start coding!

### In Git-bash (Windows)
- Get it working from **Git Bash**
  - if the command ``type python`` gives you a path, then proceed
    - otherwise you may have to do a new installation
    - or find the path
    - if anaconda installation you may add something like this:
    - ``echo 'export PATH="<path/to/Anaconda/root>:<path/to/anaconda/root>/Scripts:$PATH:' >> .bashrc``
      - example:  ``/c/Users/bjcar425/AppData/Local/anaconda3:/c/Users/bjcar425/AppData/Local/anaconda3/Scripts``
  - ``$ alias python='winpty python.exe'``
  - ``$ python -V``
    - does it give you the python version 3-something?
 - Make it permanent
 -``$ echo "alias python='winpty python.exe'" >> ~/.bashrc``

## PlantUML
- We will use the tool PlantUML to render UML code to graphical diagrams and flowcharts. 
- If you want PlantUML to render directly from a file on GitHub please install the **extension PlantUML viewer to your web browser**.
- works for multiple browsers [https://github.com/marcozaccari/markdown-diagrams-browser-extension](https://github.com/marcozaccari/markdown-diagrams-browser-extension)
   - Restart browser after installation!  
-  if the above does not work try
   - Firefox: PlantUML visualizer (is not compatible with !theme _none_ tag)
   - Chrome: Pegmatite,PlantUML viewer
   - Microsoft Edge Markdown Diagrams
- When done you should see the code below as a diagram.

```plantuml
@startuml
!theme superhero
title:"USECASE Diagrams"
skinparam actorStyle awesome
Lecturer -d->(Present slides on UML)
Participant-d->(learn UML from SLIDES)
@enduml
```
