Output = ".".join(Input.split(".")[:-1])
Output += f"_sl{Random_String}.wav"
WAV = mFile(Input).info

#-=-=-=-#

args.channels = args.c

if args.channels == "mono":
	Channels = "-ac 1"
if args.channels == "stereo":
	Channels = "-ac 2"
if args.channels == "invert":
	Channels = '-af "pan=stereo|c0=c1|c1=c0"'
if args.channels == "left":
	Channels = '-af "pan=mono|c1=FL"'
if args.channels == "right":
	Channels = '-af "pan=mono|c0=FR"'
if args.channels == "side":
	Channels = '-af "aeval=val(0)|-val(1)" -ac 1'
if not args.channels:
	Channels = Get_Channels(Input)

if not args.bit_depth:
	Bit_Depth = WAV.SIZE

SampleRate = WAV.sample_rate
if args.samplerate:
	SampleRate = floor(Number_Suffix(args.samplerate))

try:
	Normalize = ""
	if args.normalize != None:
		Normalize = " --norm=" + str(abs(args.normalize) * -1)
except ValueError:
	pass

#-=-=-=-#

Channels = str(Channels)
Bit_Depth = str(Bit_Depth)
Samplerate = str(SampleRate)