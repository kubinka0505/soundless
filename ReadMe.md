<p align=center><img src=https://raw.githubusercontent.com/kubinka0505/soundless/master/Documents/Pictures/soundless.svg width=625></p>

<p align=center><a href=https://github.com/kubinka0505/soundless/commit><img src=https://img.shields.io/github/last-commit/kubinka0505/soundless?style=for-the-badge></a>　<a href=https://github.com/kubinka0505/soundless/issues><img src=https://img.shields.io/github/issues/kubinka0505/soundless?style=for-the-badge></a>　<a href=https://github.com/kubinka0505/soundless/blob/master/License.txt><img src=https://img.shields.io/github/license/kubinka0505/soundless?logo=readthedocs&color=red&logoColor=white&style=for-the-badge></a></p>

<p align=center><img src=https://img.shields.io/tokei/lines/github/kubinka0505/soundless?style=for-the-badge>　<img src=https://img.shields.io/github/languages/code-size/kubinka0505/soundless?style=for-the-badge>　<a href=https://app.codacy.com/gh/kubinka0505/soundless/dashboard><img src=https://img.shields.io/codacy/grade/1b0ce42be58a4fe0ac00e38d8bbbd354?logo=codacy&style=for-the-badge></a></p>

## Description 📝
Pack of scripts that provides customizable optimization of `WAV` files. 

## Features 📋
| Description | Note
|:-:|:-:|
| **Automatic channels detection**<span>*</span> 🎧 | Configurable ⚙️
| **Metadata removal** 📋 |
| **Peak [Normalization](https://wikipedia.org/wiki/Audio_normalization)**<span>*</span> 🔊 | Configurable ⚙️
| **Recursive processing**<span>*</span> 📁 |
| *In-place* file processing ⚙️ | No backup ❌🗃️

<span>*</span> - Optional

## Requirements 📥
Programs:
- [`Python >= 3.5`](https://www.python.org/downloads) 🐍

Modules:
- [`filedate >= 2.0`](https://github.com/kubinka0505/filedate) - Files dates keeping 📅
- [`sty >= 0.0.4`](https://github.com/feluxe/sty) - Colored terminal output 🎨
- [`Pillow >= 5.1`](https://github.com/python-pillow/Pillow) - Colors fetching 🎨
- [`mutagen >= 1.45.1`](https://github.com/quodlibet/mutagen) - Sample rate handling 📈
- [`pyshortcuts >= 1.8`](https://github.com/newville/pyshortcuts) - Shortcuts making 📁

Packages (bold links are **Windows** static executable binaries):
- [**`SoX`**](https://sourceforge.net/projects/sox/files/sox) - Optimization, normalization and sample rate correction ⚙️
- [**`FFmpeg >= 4.2`**](https://videohelp.com/software/ffmpeg/old-versions) - Mono detection 🎧
- [`Python3-PIP`](http://packages.debian.org/sid/python3-pip)</a><span>*</span>
- [`Python3-TK`](http://packages.debian.org/sid/python3-tk)</a><span>*</span>

<span>*</span> - Required on Linux

---
## Installation 📝
**When on Linux**, install required packages by using this one-liner:
```bash
sudo apt-get install git python3-apt python3-pip python3-tk ffmpeg sox
```
1. Clone the repository and move to its directory.
	```bash
	git clone http://github.com/kubinka0505/soundless
	cd soundless
	```
2. Install required modules by inputting `pip install -r requirements.txt`

---
## Usage 📝
Optimize `WAV` file
```bash
soundless.py -i "Sample.wav"
```

As above, but from URL, [**peak-normalize**](https://wikipedia.org/wiki/Audio_normalization) file to `-3` decibells (`-n`) and change sample-rate to `32 000` hertz. (`-sr`)
```bash
soundless.py -i http://example.org/File.wav -n 3 -sr 32k
```

Optimize `WAV` files in a directory, **set the bit depth** to `24` (`-b`) and **extract left channel to mono**. (`-c`)
```bash
soundless.py -i "~/Music" -b 24 -c left
```

As above, but **process all files in subdirectories** (`-R`) and **suppress all console output** (`-q`).
```bash
soundless.py -i "%UserProfile%/Desktop/WAV" -R -q
```
---

## Meta Info ℹ️
All versions of this project have been tested on:
| OS | Distribution | OS Version | Python Version | System Architecture (`bits`) |
|:-:|:-:|:-:|:-:|:-:|
Windows | ― | 10 | 3.7.6 | 32, 64 |
Linux | Ubuntu | LTS 20.04 | 3.8.10 | 64 |