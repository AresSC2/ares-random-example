# Ares-sc2 Random Example Bot

[ares-sc2 repo](https://github.com/AresSC2/ares-sc2) <br>
[ares-sc2 docs](https://aressc2.github.io/ares-sc2/index.html)

## About
This bot is designed to showcase the fundamental processes within ares-sc2. It has been 
intentionally structured within a single file for easy comprehension (check `bot/main.py`). Where
possible the logic is race agnostic resulting in a competitive random bot in just a few 
hundred lines of code!

Feel free to 
clone this repository, or utilize the [blank starter bot](https://github.com/AresSC2/ares-sc2-starter-bot) 
as a foundation to build upon.

Take note of the terran_builds.yml, protoss_builds.yml, and zerg_builds.yml files, where 
the initial build orders are defined. The presence and correct formatting of these 
files activate the internal build runner system in ares-sc2. If creating your own bot
these files are optional.

## Installing

<b>Note, it might be easier to start from a blank template. Use the
[blank starter bot](https://github.com/AresSC2/ares-sc2-starter-bot)
and follow the instructions there if desired.</b>

Ensure you have the following setup on your local system:
- [Python 3.11](https://www.python.org/downloads/release/python-3110/) 
- [Poetry](https://python-poetry.org/) `pip install poetry`
- [Git](https://git-scm.com/)
- [Starcraft 2](https://starcraft2.com/en-gb/)
- [Maps](https://sc2ai.net/wiki/maps/) Ensure maps are moved to the correct folder as suggested in this wiki.

Clone the repository locally to your system, ensuring you include the `--recursive` flag:

`git clone --recursive https://github.com/AresSC2/ares-random-example`

 - Open a terminal or console window.

 - Navigate to the root of your bot's directory:

`cd ares-random-example`

 - Install dependencies, compile Cython, and create a new isolated virtual environment:

`poetry install`

## Run

If you have a non-standard starcraft installation or are using Linux, please adjust `MAPS_PATH` in `run.py`.

`poetry run python run.py`

## Start building your own bot

- In `config.yml` set your bots name and race
```yml
MyBotName: AresRandomExample
MyBotRace: Random
```
- Start making your own opening builds in the appropriate `yml` file: 
`terran_builds.yml`, `protoss_builds.yml` or `zerg_builds.yml`. Or remove the files
if you prefer not to use the ares build runner system.
- Create your own masterpiece in `bot/main.py`

## Updating `ares-sc2`
With a console or terminal run the following in the root of the bots' directory:

`python scripts/update_ares.py`

## Uploading to [AiArena](https://www.sc2ai.com)

<b>TLDR:</b> On each push to `main` there is a Github Actions workflow that builds a ladder ready zip. Take a 
look on the `Actions` tab to download.

Included in this repository is a convenient script named `scripts/create_ladder_zip.py`. 
However, it is important to note that the AIarena ladder infrastructure operates specifically 
on Linux-based systems. Due to the dependency of ares-sc2 on cython, it is necessary to execute 
this script on a Linux environment in order to generate Linux binaries.

To streamline this process, a GitHub workflow has been integrated into this repository when pushing to `main` 
on your GitHub repository (if you previously created a template from the 
[starter-bot](https://github.com/AresSC2/ares-sc2-starter-bot)). 
Upon each push to the main branch, the `create_ladder_zip.py` script is automatically executed on a 
Debian-based system. As a result, a compressed artifact named `ladder-zip.zip` is generated, 
facilitating the subsequent upload to AIarena. To access the generated file, navigate to the Actions tab, 
click on an Action and refer to the Artifacts section. Please note this may take a few
minutes after pusing to the `main` branch.
