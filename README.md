# Randomly Intermittent Reward Timing (RIRT)

| Feature | Tools |
|---|---|
| Languages | [![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=ffdd54)](https://www.python.org/downloads/release/python-370/) |
| Git | [![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org) |
| Formatting | [![Black](https://img.shields.io/badge/Code%20Style-black-000000)](https://github.com/psf/black) [![docformatter](https://img.shields.io/badge/Docstring%20Formatter-docformatter-fedcba.svg)](https://github.com/PyCQA/docformatter) [![numpy](https://img.shields.io/badge/Docstring%20Style-numpy-459db9.svg)](https://numpydoc.readthedocs.io/en/latest/format.html) [![Imports: isort](https://img.shields.io/badge/%20Imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/) |

RIRT is a small, pip-installable script built with only base python that can be run to decide probabilistically if you get a reward for doing something.

This concept comes from the [*Huberman Lab*](https://hubermanlab.com/) podcast:

> **Use (Randomly) an Intermittent Reward Timing (RIRT)** [to manage dopamine peaks]. This is the most powerful schedule for dopamine release and **staying motivated**. The casinos use it to take people’s money. It works 100% of the time. You can use RIRT to your advantage, to stay motivated in any pursuit. The key is to **celebrate your wins, but do not celebrate every win**. When you succeed in reaching a milestone, sometimes enjoy that; other times (at random), just keep going. Even better, associate “winning” with the effort process itself. That’s the holy grail of dopamine management for success. It won’t make you dull or unhappy; it will make everything easier and more pleasurable, without the peaks and valleys of dopamine that external-reward-driven people experience, and you’ll obtain all the external rewards anyway.

After installation, you can run `rirt` in your terminal every time you reach some milestone to see if you should reward yourself. By default, `rirt` runs with a probability of 0.85, but you can set this probability to anything you want by using `-p` and passing a float between 0 and 1.
