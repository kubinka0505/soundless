Size_In = os.path.getsize(Input)

#-=-=-=-#

Command_FFmpeg = f'{FFmpeg} -i "{Input}" -compression_level 12 -fflags +bitexact -flags:a +bitexact -map 0 -map_metadata 0:s:0 "{Output}"'
Command_SoX = f'{SoX} "{Output}" -D -L -b {Bit_Depth} -c {Channels} -r {SampleRate}{Normalize} --comment "" -G "{Input}"'

os.system(Command_FFmpeg)
os.system(Command_SoX)

#-=-=-=-#

Size_Out = os.path.getsize(Output)
Percentage = "0.00" if Size_In == Size_Out else round((100 - (Size_Out / Size_In) * 100), 2)

print("\n{4}{0}{8}\n\tOptimized from {6}{1}{8} -> {5}{2}{7}\t\t{7}{3}%{8}".format(
	FilePath(Input).censor(),
	File_Size(Size_In), File_Size(Size_Out), Percentage,

	Styles.Meta_Info,
	Styles.OK, Styles.Flaw,
	Styles.Info if str(Percentage) != "0.00" else Styles.Error,
	Styles.Reset
	)
)

#-=-=-=-#

os.remove(Output)