A python game modeled after "kings" or "kings cup" I've also heard it called. Meant to bring social gaming into drinking games.

- Never drink alone again!

Install instructions:

On windows:
	I'm sorry but y'all are on your own. I honestly have been removed from windows too long to offer
	good instructions for it. If you REALLY have issues with it, shoot me a message cause I've done
	it before, just dont want to look it up right now.

On *nix:
	first, make sure your on python 2.X because I haven't coded up for 3.X yet. I'm working on it,
	give me a break.

	1) - so if you have python, you can run this:
		# pip install pygame
	2) from there, decide where you want to game to run. Typical places are your homedir, so you may
	want to make a directory on your desktop or somewhere easy to access. heres how I do it:
	
	# cd ~/Desktop; git clone https://github.com/jay13jay/kings_connected; cd ~/Desktop/kings_connected
	this assumes you have a folder named Desktop in your home dir, which most distros do I think.
	it then drops you into the actual game folder. This is all the "install" that is needed, provided
	that you have pygame installed. 
	
	INSTRUCTIONS:
	https://www.pygame.org/install.html
	
	On linux, if you have pip (RHEL package python-pip) than you can just run this:
	# pip install pygame

	If you Don't, you need to install it. On RHEL, you can just do:
	# yum install pyton-pip


	Regardless of how you get it, get pygame, then move on to the next steps.
	
	Download the actual game:
	# git clone https://github.com/jay13jay/kings_connected

	Once the game is installed, you can run it by going into the folder (~/Desktop/kings_connected or
	wherever you cloned the game to) and type the following:
	
	# python kings.py


TODO:

1) set up a menu system to configure the game

2) set up logic for multiple players

3) set up database for cards so there are no repeats
	have option for continuous flow, always random card or 52 cards spread out, or 52 card stacked deck (in order top -> bottom)

4) set up collision detection
	** priority. needs to be done before anything else

	curl -s httpd://identity.api.rackspacecloud.com/v2.0/tokens -X 'POST' -d '{"RAX-KSKEY:apiKeyCredentials":
