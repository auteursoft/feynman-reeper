# Feynman Reeper (Or, Фейнман Рипер, for the MAGA user. 🤣)
A python program that downloads mp3 files of the audio of the Feynman lectures on physics from Cal Tech.

The directory `feynman_audio` contains the actual mp3 files this downloads retrieved using `harvest.py` on May 16, 2025 from a secret location in Finland. This is nominally important since, presumably, the page we retrieved the files from may or may not "always be there" in the same structure for which it worked on this day. 

The more generalizable utility of this repository is that it deals with most of the common measures deployed on websites that would prevent the systematic downloading of "all the files". Questions about fair use, copyright, or other matters? Well, I'm an American in 2025 and near as I can tell my government no longer gives a flying f*** about these things because OpenAI is [Jesus, etc.](https://www.youtube.com/watch?v=USMsgVbf8Us) Also, think of it this way: That same government is more likely to shut down Cal Tech than they are to care about copyright infringement. Furthmore, during a summoning of Feynman's soul, I was granted direct permission to use and preserve his lectures against my own fascist leaning government. 

## Setup

1. Make sure you have Python 3 loaded on your computer. This code was implemented and tested using Python 3.13.12 on an Apple Silicon Macbook Pro (circa 2023). Full Hardware ID: 
```
Model Name:	MacBook Pro
Model Identifier:	Mac14,6
Model Number:	MNXA3JA/A
Chip:	Apple M2 Max
Total Number of Cores:	12 (8 performance and 4 efficiency)
Memory:	64 GB
System Firmware Version:	11881.101.1
OS Loader Version:	11881.101.1
Serial Number (system):	H460JG96WY
Hardware UUID:	AF186476-E8CF-5BF8-A2C2-6CC968E02DAE
Provisioning UDID:	00006021-000230DA3A43C01E
Activation Lock Status:	Enabled
```

2. Clone this repository. Fork it first if you want to make contributions. 
3. Create a python virtual environment: `python3 -m venv .venv`
4. Activate the Python virtual environment: `source .venv/bin/activate`
5. Add the necessary external libraries to your Python virtual environment: `pip install -r requirements.txt`
6. Run `harvest.py`: `python harvest.py`: Note the first step will be to create an mp3 inventory file named `flptapes.js`. The version of that file generated when this repository was created is preserved for comparison and future change analysis in the `_flptapes.js` file included in this repository. 


© 2025, Professor Doctor Sean P. Goggins, the Dork Union, and ["Mr. Hand's Songs of Spicolli"](https://open.spotify.com/playlist/2aOikiOH69uiC9VHIAODA6?si=d9c7ac2492bf43fa)