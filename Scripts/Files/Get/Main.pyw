Glob = "*"
if args.recursive:
	Glob += "*/*"

print()
	
#-=-=-=-#

if not URL:
	if isinstance(args.input, tuple):
		Files = list(args.input)
	else:
		Files = []
		if os.path.exists(args.input):
			if os.path.isfile(args.input):
				Files = [args.input]
			else:
				Latest_Directory = os.path.abspath(args.input)
				#-=-=-=-#
				for File in Path(args.input).glob(Glob):
					File = str(File.resolve())
					Format = File.split(".")[-1].lower()
					if Format == "wav":
						Files += [File]
		else:
			raise Error(f'File doesn\'t exist! ({args.input})')
else:
	File = os.path.join(
		FilePath("~/Documents").get(),
		args.input.split("/")[-1]
	)
	with get(args.input, stream = 1) as Site:
		if Site.ok:
			if Site.headers["content-type"].lower().endswith("wav"):
				with open(File, "wb") as File_:
					for Chunk in Site.iter_content(chunk_size = 4096): 
						File_.write(Chunk)
			else:
				raise Error("Invalid file type")
		else:
			raise Error("URL returned status code {0} - {1}.".format(
				Site.status_code, Site.reason.title()
				)
			)
		Files = [File]

#-=-=-=-#

if not Files:
	raise Error("No WAV files in given directory")

if not URL:
	if len(Files) < 2:
		if mFile(Files[0]).mime[0].split("/")[-1] != "wav":
			raise Error("Not an WAV file")
	else:
		Files = sorted(Files, key = len)

#-=-=-=-#

with redirect_stdout(stdout):
	print(f"\n{Break}\n\nFiles to process")
	for File in Files:
		print("\t" + Styles.Meta_Info_2 + FilePath(File).censor(), Styles.Reset)
		sleep(1 / 40)
	print()