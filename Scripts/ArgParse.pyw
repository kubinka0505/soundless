Parser = ArgumentParser(
	description = "WAV optimizer",
	add_help = 0,
	formatter_class = \
		lambda prog, size = float("inf"): \
			HelpFormatter(
				prog,
				width = size,
				max_help_position = size
			)
	)


#-=-=-=-#

Required = Parser.add_argument_group("Required arguments")

Input = Required.add_argument(
	"-i", "--input",
	type = str,
	metavar = '"str"',
	required = 1,
	help = "File path or directory to optimize files in"
)

#-=-=-=-#

Optional = Parser.add_argument_group("Optional arguments")

Optional.add_argument(
	"-c", #"--channels",
	type = str,
	choices = [
		"mono", "stereo", "invert",
		"left", "right",
		"side"
	],
	default = 0,
	help = Styles.Info + "Ignore to auto-detect"
)

Optional.add_argument(
	"-r", "--samplerate",
	type = str,
	metavar = "int",
	default = 0,
	help = Styles.Info + "Ignore to copy"
)

Optional.add_argument(
	"-b", "--bit_depth",
	type = int,
	choices = [16, 24, 32],
	default = 0,
	help = Styles.Info + "Ignore to copy"
)

Optional.add_argument(
	"-n", "--normalize",
	type = float,
	metavar = "float",
	default = None,
	help = f"Normalize to given value. (dBFS) {Styles.Error}Result is always negative"
)

Optional.add_argument(
	"-h", "--help",
	default = SUPPRESS,
	action = "help",
	help = "Displays this message"
)

#-=-=-=-#

Switch = Parser.add_argument_group("Optional switch arguments")

Switch.add_argument(
	"-R", "--recursive",
	action = "store_true",
	help = "Include files in subdirectories"
)

Switch.add_argument(
	"-q", "--quiet",
	action = "store_false",
	help = "Supress console output"
)

#-=-=-=-#

for Argument in Parser._actions:
	Argument.help += "." + Styles.Reset

args = Parser.parse_args()

URL = 0
if "://" in args.input:
	URL = 1
else:
	args.input = FilePath(args.input).get()

stdout = None
if args.quiet:
	stdout = os.sys.stdout