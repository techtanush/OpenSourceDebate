# Opening your files in CardMirror (required)

The `.docx` files this toolkit builds carry their formatting in Word styles: the Pocket/Hat/Block/Tag hierarchy, the bold short cite, the cyan highlight, and the 8pt unread text. **You must open them in CardMirror (or Verbatim in Microsoft Word) to see and use that formatting.**

Plain viewers will **not** show it. TextEdit, macOS Quick Look, Pages, and most preview panes ignore Word styles, so they show a flat wall of text and may drop the highlighting. If a file looks unformatted there, nothing is wrong with it. Open it in CardMirror.

**CardMirror** is a free, open-source debate editor that reads and writes the same `.docx` files as Verbatim without needing Word. This repo's authors do not maintain it. Get it from the official sources below, not from a fork.

- Official site / web app: https://cardmirror.app/
- Source and downloads: https://github.com/ant981228/cardmirror (see the **Releases** page)
- User manual: https://github.com/ant981228/cardmirror/blob/main/MANUAL.md

## Install

Pick one. The web app needs nothing installed.

### Web app (any computer, including Chromebooks)

1. Open https://cardmirror.app/ in **Chrome, Edge, or another Chromium browser**.
2. Optional: click the **Install** button in the address bar to add it as an app.

Saving a file in place only works in Chromium browsers. In Firefox and Safari, Save downloads a copy instead.

### macOS

1. Go to https://github.com/ant981228/cardmirror/releases and download `CardMirror-x.x.x-universal.dmg` (one file for Apple Silicon and Intel).
2. Open the `.dmg` and drag **CardMirror** into **Applications**.
3. First launch only, because the app is unsigned:
   - If macOS says it "can't be opened because Apple cannot check it for malicious software," right-click (or Control-click) **CardMirror** in Applications and choose **Open**.
   - If it says the app "is damaged and can't be opened," run this in Terminal, then enter your password:

```bash
sudo xattr -cr /Applications/CardMirror.app
```

### Windows

1. Download `CardMirror Setup x.x.x.exe` from the Releases page and run it.
2. First launch only: if "Windows protected your PC" appears, click **More info**, then **Run anyway**.

### Linux

```bash
# AppImage
chmod +x cardmirror-x.x.x.AppImage
./cardmirror-x.x.x.AppImage
```

```bash
# Arch-based (AUR)
yay -S cardmirror-bin        # or: paru -S cardmirror-bin
```

```bash
# Arch-based (downloaded package)
sudo pacman -U cardmirror-x.x.x.pacman
```

Replace `x.x.x` with the version you downloaded. Check the Releases page for the current file names, since they change with each release.

## Using files from this toolkit

1. Build a file: `python tools/build_docx.py cards.md -o cards.docx`
2. In CardMirror, choose **Open...** and pick `cards.docx` (it accepts `.docx` and its own `.cmir` format).
3. Check the structure and marking (see below).
4. Cut, edit, and send to your speech doc from there. Save as `.docx` to share with Verbatim users.

### What you should see

- The outline shows **Pocket > Hat > Block > Tag** (CardMirror's F4, F5, F6, F7 heading levels).
- The short cite (`Lastname YY`) is bold and larger; the rest of the cite line is small.
- Read text is **underlined with a highlight**.
- Unread context is small (8pt), with no underline.

### If the styles look wrong

CardMirror's landing page has a **Clean styles** button ("Clean a .docx file's styles to the Verbatim standard"). Run your generated file through it, then open it. If something still looks off, run `python tools/inspect_docx.py cards.docx` and check the style counts, then open an issue with the file attached.

## Handy CardMirror shortcuts

From the CardMirror manual (`Mod` is Ctrl on Windows/Linux and Cmd on Mac; check Settings if your version differs):

| Action | Key |
|--------|-----|
| Pocket / Hat / Block / Tag | F4 / F5 / F6 / F7 |
| Analytic / Undertag | Mod-F7 / Mod-F8 |
| Cite (author last name and date) | F8 |
| Underline | F9 or Mod-U |
| Emphasis (boxed) | F10 |
| Highlight | F11 |
| Condense | F3 |
| Shrink unread text | Mod-8 |
| Clear formatting | F12 |

Cutting by hand in CardMirror is still the final step for many debaters. The toolkit gets the research, tags, cites, and a first pass of the marking done; you adjust highlighting in the editor.

## Things to know

- **License:** CardMirror is under the PolyForm Noncommercial License 1.0.0, so noncommercial use is permitted and commercial use needs a separate license. That license applies to CardMirror, not to this repo.
- **Stability:** the CardMirror project describes itself as stable and used daily, but also advises keeping a copy of anything critical in a second format. Do that for tournament files.
- **Forks:** several forks exist with extras (multi-pane views, team collaboration). The upstream repo above is the safest starting point.
- **Verbatim in Word** also works. Open the `.docx` in Word with the Verbatim add-in installed, and the Debate ribbon and styles will apply.
- **Not yet tested here:** this toolkit's generated files have been checked with its own inspector and unit tests, not yet opened in CardMirror or Word by the maintainers. If you open one and something is off, please report it.
